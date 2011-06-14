# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan, PaperRoll, PaperHistory
from django.core.cache import cache
from datetime import datetime

import socket

def maxclamp(request):
# Query tag ID, paper code, and size for assigning tag #
	tagiddomain = range(1,10000)
	tagidquery = PaperRoll.objects.values_list('tarid')
	tagidlist = PaperRoll.objects.values_list('tarid', flat=True).order_by('-tarid')
	for tag in tagidlist:
		if tag in tagiddomain: tagiddomain.remove(tag)
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

		try:
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
			datum = soc.recv(32)

			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				resp = soc.recv(8192)
				if resp.find("tag_id") > -1:
					cache.set('data', resp, 10) # Wait 10 seconds for 'data' to expire...
					timestamp = datetime.now().strftime("%H:%M:%S")
					cache.set('timestamp', timestamp, 10)

			soc.close()
		except:
			socror = 'Cannot connect to RFID reader.'

		data = cache.get('data')
		lasttime = cache.get('timestamp')
		tagdata = str(data).split("\r\n")

		if len(tagdata) > 0:
			idlist = list()
			loclist = list()

			for tag in tagdata:
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
				toperror = "No location tag in field."

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if len(repeat_AA) > 0:
				if max(repeat_AA) in repeat_AA:
					n = repeat_AA.index(max(repeat_AA))
					realtag = tagid_A[n][7:11]
					tag2write = tagid_A[n][6:30]

					if tag2write.count('0') < 15 or PaperRoll.objects.filter(tarid=realtag).exists() == False:
						writeMode = 'new'
					elif tag2write.count('0') >= 15:
						writeMode = 'reused'

# Query database from realtag #
					if PaperRoll.objects.filter(tarid=realtag).exists() == True:
						rtquery = PaperRoll.objects.get(tarid=realtag)
						paper_roll_id = rtquery.tarid
						paper_code = rtquery.paper_code
						size = rtquery.width
						unit = rtquery.wunit
						initial_weight = rtquery.initial_weight
						temp_weight = rtquery.temp_weight
						lane = rtquery.lane
						position = rtquery.position

						hquery1 = PaperHistory.objects.filter(roll_id=realtag).exists()

						if hquery1 == True:
							hquery2 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
							hquery2list = list(hquery2)
							actual_wt = hquery2list[0]
						else:
							actual_wt = initial_weight
							undo_btn = ""
					else:
						realtag = 'unknown'

	if operating_mode == 'fake':

		atlane = '2'
		atposition = '5'
		atlocation = 'Stock'

#		realtag = '1223'
#		tag2write = '112233445566778899AABBCC'

		realtag = '0065'
		tag2write = '30065AAAA000000000000000'

		if tag2write.count('0') < 15 or PaperRoll.objects.filter(tarid=realtag).exists() == False:
			writeMode = 'new'
		elif tag2write.count('0') >= 15:
			writeMode = 'reused'
		lasttime = datetime.now().strftime("%H:%M:%S")

		if PaperRoll.objects.filter(tarid=realtag).exists() == True:
			rtquery = PaperRoll.objects.get(tarid=realtag)
			paper_roll_id = rtquery.tarid
			paper_code = rtquery.paper_code
			size = rtquery.width
			unit = rtquery.wunit
			initial_weight = rtquery.initial_weight
			temp_weight = rtquery.temp_weight
			lane = rtquery.lane
			position = rtquery.position

			hquery1 = PaperHistory.objects.filter(roll_id=realtag).exists()

			if hquery1 == True:
				hquery2 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
				hquery2list = list(hquery2)
				actual_wt = hquery2list[0]
			else:
				actual_wt = initial_weight
				undo_btn = ""
		else:
			realtag = 'unknown'

	return render_to_response('maxclamp.html', locals())

### UPDATE ###
def maxupdate(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	if 'temp_weight' in request.GET and request.GET['temp_weight']:
		temp_weight = request.GET['temp_weight']

	if 'actual_wt' in request.GET and request.GET['actual_wt']:
		actual_wt = request.GET['actual_wt']

	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=temp_weight, timestamp=now)
	p.save()

	return HttpResponseRedirect('/django/maxclamp/')

### UNDO ###
def maxundo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()

	return HttpResponseRedirect('/django/maxclamp/')

def maxchangeloc(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	if 'lane' in request.GET and request.GET['lane']:
		ilane = request.GET['lane']

	if 'pos' in request.GET and request.GET['pos']:
		ipos = request.GET['pos']

	PaperRoll.objects.filter(tarid=realtag).update(lane=ilane, position=ipos)

	return HttpResponseRedirect('/django/maxclamp/')

def maxassigntag(request):
	if 'atagid' in request.GET and request.GET['atagid']:
		atagid = int(request.GET['atagid'])
		if len(str(atagid)) == 1: stratagid = '000'+str(atagid)
		if len(str(atagid)) == 2: stratagid = '00'+str(atagid)
		if len(str(atagid)) == 3: stratagid = '0'+str(atagid)

	if 'apcode' in request.GET and request.GET['apcode']:
		apcode = request.GET['apcode']

	if 'asize' in request.GET and request.GET['asize']:
		asize = int(request.GET['asize'])

	if 'aweight' in request.GET and request.GET['aweight']:
		aweight = int(request.GET['aweight'])

	if 'alane' in request.GET and request.GET['alane']:
		alane = request.GET['alane']
	else:
		alane = ''

	if 'aposition' in request.GET and request.GET['aposition']:
		aposition = int(request.GET['aposition'])
	else:
		aposition = None

	if 'atag2write' in request.GET and request.GET['atag2write']:
		atag2write = request.GET['atag2write']


	if stratagid and apcode and asize and aweight and atag2write:
		if str(stratagid) == str(atag2write[1:5]):
			PaperRoll.objects.filter(tarid=atagid).update(paper_code=apcode, width=asize, wunit='inch', initial_weight=aweight, lane=alane, position=aposition)
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
					p = PaperRoll(tarid=atagid, paper_code=apcode, width=asize, wunit='inch', initial_weight=aweight, lane=alane, position=aposition)
					p.save()
				if atag2write.count('0') >= 15:
					p = PaperRoll(tarid=atagid, paper_code=apcode, width=asize, wunit='inch', initial_weight=aweight, lane=alane, position=aposition)
					p.save()
					tag2del = int(atag2write[1:5])
					q = PaperRoll.objects.filter(tarid=tag2del)
					q.delete()
			else:
				return render_to_response('intmed.html', locals())

	return HttpResponseRedirect('/django/maxclamp/')
