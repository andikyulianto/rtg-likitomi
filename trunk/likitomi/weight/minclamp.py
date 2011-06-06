# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan, PaperRoll, PaperHistory
from django.core.cache import cache
import datetime

import socket

def minclamp(request):
	try:

# Query tag ID, paper code, and size for assigning tag #
		tagiddomain = range(1,10000)
		tagidquery = PaperRoll.objects.values_list('id')
		tagidlist = PaperRoll.objects.values_list('id', flat=True).order_by('-id')
		for tag in tagidlist:
			tagiddomain.remove(tag)
		avaitag = tagiddomain[0]

		scursor1 = connection.cursor()
		scursor1.execute("""
			SELECT DISTINCT paper_code
			FROM weight_paperroll
			ORDER BY paper_code""")
		spcode = scursor1.fetchall()
		spcodelist = list()
		for pcode in spcode:
			spcodelist.append(pcode[0])
		scursor2 = connection.cursor()
		scursor2.execute("""
			SELECT DISTINCT width
			FROM weight_paperroll
			ORDER BY width""")
		swidth = scursor2.fetchall()
		swidthlist = list()
		for width in swidth:
			swidthlist.append(width[0])

# RFID: paper roll and location tags #
		operating_mode = 'real' # Operating mode = {'real', 'fake'}

		if operating_mode == 'real':

			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			## soc.send('setup.operating_mode = standby\r\n')
			soc.send('tag.db.scan_tags(100)\r\n')
			datum = soc.recv(128)

			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				resp = soc.recv(8192)
				if resp.find("tag_id") > -1:
					cache.set('data', resp, 10) # Wait 10 seconds for 'data' to expire...
					timestamp = datetime.datetime.now().strftime("%H:%M:%S")
					cache.set('timestamp', timestamp, 10)

			data = cache.get('data')
			lasttime = cache.get('timestamp')
			tagdata = data.split("\r\n")

			idlist = list()
			loclist = list()

			for tag in tagdata:
#				if "AAAA" in tag:
#					idlist.append(tag)
#				if "BBBB" in tag:
#					loclist.append(tag)
#				if "type=STG" in tag or "AAAA" in tag:
#					idlist.append(tag)
#				if "type=ISOC" and "AAAA" not in tag or "BBBB" in tag:
#					loclist.append(tag)
				if "BBBB" in tag:
					loclist.append(tag)
				else:
					idlist.append(tag)

			cnt = 0

			tagid_A = list()
			type_A = list()
			antenna_A = list()
			repeat_A = list()
			last_A = list()

			for id1 in idlist:
				id2 = id1.replace("(","")
				id2 = id2.replace(")","")
				id3 = id2.split(", ")
				for id4 in id3:
					id5 = id4.split("=")
					if id5[0]=="tag_id":tagid_A.append(id5[1])
					elif id5[0]=="type":type_A.append(id5[1])
					elif id5[0]=="antenna": antenna_A.append(id5[1])
					elif id5[0]=="repeat": repeat_A.append(id5[1])
					elif id5[0]=="last": last_A.append(id5[1])
					cnt= cnt+1

			tagid_B = list()
			type_B = list()
			antenna_B = list()
			repeat_B = list()

			for loc1 in loclist:
				loc2 = loc1.replace("(","")
				loc2 = loc2.replace(")","")
				loc3 = loc2.split(", ")
				for loc4 in loc3 :
					loc5 = loc4.split("=")
					if loc5[0]=="tag_id": tagid_B.append(loc5[1])
					elif loc5[0]=="type": type_B.append(loc5[1])
					elif loc5[0]=="antenna": antenna_B.append(loc5[1])
					elif loc5[0]=="repeat": repeat_B.append(loc5[1])
					cnt= cnt+1

			lan = 0
			pos = 0
			totalCount = 0

			if len(repeat_B) > 0 :
				cnt = 0
				for rep in repeat_B:
					if type_B[cnt] == "ISOC":
#						lindex = int(tagid_B[cnt][26:28])
						prelindex = tagid_B[cnt][25:27]
						if prelindex == 'AB': lindex = 1
						if prelindex == 'CD': lindex = 2
						if prelindex == 'EF': lindex = 3
						if prelindex == 'FF': lindex = 4
						if prelindex == 'CC': lindex = 0
						if prelindex == 'DD': lindex = 5
						pindex = int(tagid_B[cnt][27:30])
						lan += float(lindex)*float(repeat_B[cnt])
						pos += float(pindex)*float(repeat_B[cnt])
						totalCount += float(repeat_B[cnt])

					cnt = cnt+1

			if totalCount > 0:
				L = int(round(lan/totalCount,0))
				P = int(round(pos/totalCount,0))
			else:
				L = 0
				P = 0

			atlane = str(L)
			atposition = str(P)
			atlocation = ''

			if L == 0:
				atlocation = 'CR'
			if L == 5:
				atlocation = 'Scale'
			if L in range(1, 5):
				atlocation = 'Stock'

			if L == 0 and P == 0:
				atlane = ""
				atposition = ""
				atlocation = ""
				toperror = "[No location tag in field.]"

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if max(repeat_AA) in repeat_AA:
				n = repeat_AA.index(max(repeat_AA))

#			tagsplt = tagid_A[n].split("AAAA")
#			realtag = int(tagsplt[1][0:4])
			realtag = tagid_A[n][7:11]
#			lasttime = last_A[n][11:19]
			tag2write = tagid_A[n][6:30]
			if tag2write.count('0') < 15:
				writeMode = 'new'
			elif tag2write.count('0') >= 15:
				writeMode = 'reused'

			soc.close()

		if operating_mode == 'fake':

			# MINCLAMP #
			atlane = '2'
			atposition = '4'
			atlocation = 'Stock'

#			realtag = '0064'
#			tag2write = '30064AAAA000000000000000'
			realtag = '1223'
			tag2write = '112233445566778899AABBCC'
			if tag2write.count('0') < 15:
				writeMode = 'new'
			elif tag2write.count('0') >= 15:
				writeMode = 'reused'
			lasttime = datetime.datetime.now().strftime("%H:%M:%S")

# Query database from realtag #
		if realtag:
			rtquery = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'width', 'wunit', 'initial_weight','temp_weight', 'lane', 'position')[0]
			rtquerylist = list(rtquery)

			paper_roll_id = rtquerylist[0]
			paper_code = rtquerylist[1]
			size = rtquerylist[2]
			unit = rtquerylist[3]
			initial_weight = rtquerylist[4]
			temp_weight = rtquerylist[5]
			lane = rtquerylist[6]
			position = rtquerylist[7]

			hquery1 = PaperHistory.objects.filter(roll_id=realtag).exists()

			if hquery1 == True:
				hquery2 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
				hquery2list = list(hquery2)
				actual_wt = hquery2list[0]
			else:
				actual_wt = initial_weight
				undo_btn = ""

# Exceptions #
	except UnboundLocalError: pass

	except ValueError: pass

	except TypeError: pass

	except: # Timeout #
		pass

	return render_to_response('minclamp.html', locals())

### UPDATE ###
@transaction.commit_manually
def minupdate(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/django/minclamp/')

	if 'temp_weight' in request.GET and request.GET['temp_weight']:
		temp_weight = request.GET['temp_weight']
	else:
		return HttpResponseRedirect('/django/minclamp/')

	if 'actual_wt' in request.GET and request.GET['actual_wt']:
		actual_wt = request.GET['actual_wt']
	else:
		return HttpResponseRedirect('/django/minclamp/')

	p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=temp_weight)
	p.save()
	transaction.commit()

	return HttpResponseRedirect('/django/minclamp/')

### UNDO ###
@transaction.commit_manually
def minundo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/django/minclamp/')

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()
	transaction.commit()

#	transaction.rollback()

	return HttpResponseRedirect('/django/minclamp/')

def minchangeloc(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		realtag = ""

	if 'lane' in request.GET and request.GET['lane']:
		ilane = request.GET['lane']
	else:
		ilane = ""

	if 'pos' in request.GET and request.GET['pos']:
		ipos = request.GET['pos']
	else:
		ipos = ""

	lquery = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'temp_weight')[0]
	lqlist = list(lquery)
	paper_code = lqlist[0]
	width = lqlist[1]
	wunit = lqlist[2]
	initial_weight = lqlist[3]
	temp_weight = lqlist[4]
	p = PaperRoll(id=realtag, width=width, wunit=wunit, initial_weight=initial_weight, temp_weight=temp_weight)
	p.paper_code = paper_code
	p.width = width
	p.wunit = wunit
	p.initial_weight = initial_weight
	p.temp_weight = temp_weight
	p.lane = ilane
	p.position = ipos
	p.save()

	return HttpResponseRedirect('/django/minclamp/')

@transaction.commit_manually
def minassigntag(request):
	try:
		if 'atagid' in request.GET and request.GET['atagid']:
			atagid = int(request.GET['atagid'])
		else:
			return HttpResponseRedirect('/django/minclamp/')
		if len(str(atagid)) == 1: stratagid = '000'+str(atagid)
		if len(str(atagid)) == 2: stratagid = '00'+str(atagid)
		if len(str(atagid)) == 3: stratagid = '0'+str(atagid)

		if 'apcode' in request.GET and request.GET['apcode']:
			apcode = request.GET['apcode']
		else:
			return HttpResponseRedirect('/django/minclamp/')

		if 'asize' in request.GET and request.GET['asize']:
			asize = int(request.GET['asize'])
		else:
			return HttpResponseRedirect('/django/minclamp/')

		if 'aweight' in request.GET and request.GET['aweight']:
			aweight = int(request.GET['aweight'])
		else:
			return HttpResponseRedirect('/django/minclamp/')

		if 'alane' in request.GET and request.GET['alane']:
			alane = request.GET['alane']
		else:
			alane = ''

		if 'aposition' in request.GET and request.GET['aposition']:
			aposition = int(request.GET['aposition'])
		else:
			aposition = 0

		if 'atag2write' in request.GET and request.GET['atag2write']:
			atag2write = request.GET['atag2write']
		else:
			return HttpResponseRedirect('/django/minclamp/')

		if str(stratagid) == str(atag2write[1:5]):
			r = PaperRoll(id=atagid)
			r.paper_code = apcode
			r.width = asize
			r.wunit = 'inch'
			r.initial_weight = aweight
			r.temp_weight = 0
			r.lane = alane
			r.position = aposition
			r.save()
			transaction.commit()
			return HttpResponseRedirect('/django/minclamp/')
		else:
			HOST = '192.41.170.55' # CSIM network
#			HOST = '192.168.101.55' # Likitomi network
#			HOST = '192.168.1.55' # My own local network: Linksys
#			HOST = '192.168.2.88' # In Likitomi factory
			PORT = 50007
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))

			soc.send('tag.write_id(new_tag_id=3'+stratagid+'AAAA000000000000000, tag_id='+atag2write+')\r\n')
			response = soc.recv(128)
			soc.close()

			if response.find('ok') != -1:
				if atag2write.count('0') < 15:
					p = PaperRoll(id=atagid, paper_code=apcode, width=asize, wunit='inch', initial_weight=aweight, lane=alane, position=aposition)
					p.save()
					transaction.commit()
				if atag2write.count('0') >= 15:
					p = PaperRoll(id=atagid, paper_code=apcode, width=asize, wunit='inch', initial_weight=aweight, lane=alane, position=aposition)
					p.save()
					tag2del = int(atag2write[1:5])
					q = PaperRoll(id=tag2del)
					q.delete()
					transaction.commit()
				return HttpResponseRedirect('/django/minclamp/')
			else:
				return render_to_response('intmed.html', locals())
		return HttpResponseRedirect('/django/minclamp/')
	except:
		pass
