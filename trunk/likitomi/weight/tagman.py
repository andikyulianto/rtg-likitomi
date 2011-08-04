# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from django.core.cache import cache
from datetime import datetime
import socket
from weight.models import PaperRolldetails, PaperMovement

#HOST = '192.41.170.55' # CSIM network
HOST = '192.168.101.55' # Likitomi's meeting room
#HOST = '192.168.1.55' # My own local network: Linksys

#HOST = '192.168.2.88' # Likitomi's factory: IMPLEMENTATION!
PORT = 50007

# RFID: paper roll and location tags #
rfid_mode = 'real' # RFID mode = {'real', 'fake'}

def tagman(request):
	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('paper_roll_detail_id')
	tagidlist = PaperRolldetails.objects.values_list('paper_roll_detail_id', flat=True).order_by('-paper_roll_detail_id')
	for tag in tagidlist:
		if tag in tagiddomain: tagiddomain.remove(tag)
	avaitag = tagiddomain[0]

	spcode = PaperRolldetails.objects.values_list('paper_code').distinct().order_by('paper_code')
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])

	swidth = PaperRolldetails.objects.values_list('size').distinct().order_by('size')
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	query = PaperRolldetails.objects.values_list('paper_roll_detail_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('rfid_roll_id','paper_roll_detail_id')

	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)

	for lst in nlist:
		roll_id = lst[0]
		if PaperMovement.objects.filter(roll_id=roll_id).exists() == True:
			current_weight = int(PaperMovement.objects.filter(roll_id=roll_id).order_by('-created_on')[0].actual_wt)
		else:
			current_weight = PaperRolldetails.objects.get(paper_roll_detail_id=roll_id).initial_weight
		lst.append(current_weight)

	if rfid_mode == 'real':
# Connect to RFID reader #
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			## soc.send('setup.operating_mode = standby\r\n')
			soc.send('tag.db.scan_tags(100)\r\n')
			datum = soc.recv(32)
			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				recv = soc.recv(8192)
				if recv.find("tag_id") > -1:
					cache.set('data', recv, 10) # Wait 10 seconds for 'data' to expire...
					timestamp = datetime.now().strftime("%H:%M:%S")
					cache.set('timestamp', timestamp, 10)
			soc.close()
		except:
			socror = 'Cannot connect to RFID reader'

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
					cnt = cnt+1

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
					cnt = cnt+1

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

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if len(repeat_AA) > 0:
				if max(repeat_AA) in repeat_AA:
					n = repeat_AA.index(max(repeat_AA))
					realtag = tagid_A[n][7:11]
					tag2write = tagid_A[n][6:30]

					if tag2write.count('0') < 15 or PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.count('0') >= 15:
						tagstatus = 'known'

					if PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == True:
						rtquery = PaperRolldetails.objects.get(paper_roll_detail_id=realtag)
						paper_roll_id = rtquery.paper_roll_detail_id
						paper_code = rtquery.paper_code
						size = rtquery.size
						unit = rtquery.uom
						initial_weight = rtquery.initial_weight
						temp_weight = rtquery.temp_weight
						lane = rtquery.lane
						position = rtquery.position
						if position == None: position = ''

						if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
							actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
						else:
							actual_wt = rtquery.initial_weight

	if rfid_mode == 'fake':

#		atlocation = 'Scale'

#		atlane = 1
#		atposition = 4
#		atlocation = 'Stock'

#		tag2write = '112233445566778899AABBCC'
		tag2write = '30065AAAA000000000000000'
		realtag = tag2write[1:5]

		lasttime = datetime.now().strftime("%H:%M:%S")

		if tag2write.count('0') < 15 or PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == False:
			tagstatus = 'unknown'
		elif tag2write.count('0') >= 15:
			tagstatus = 'known'

		if PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == True:
			rtquery = PaperRolldetails.objects.get(paper_roll_detail_id=realtag)
			paper_roll_id = rtquery.paper_roll_detail_id
			paper_code = rtquery.paper_code
			size = rtquery.size
			unit = rtquery.uom
			initial_weight = rtquery.initial_weight
			temp_weight = rtquery.temp_weight
			lane = rtquery.lane
			position = rtquery.position

			if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
				actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
			else:
				actual_wt = rtquery.initial_weight

	return render_to_response('tagman.html', locals())

def showtaglist(request):
	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('paper_roll_detail_id')
	tagidlist = PaperRolldetails.objects.values_list('paper_roll_detail_id', flat=True).order_by('-paper_roll_detail_id')
	for tag in tagidlist:
		if tag in tagiddomain: tagiddomain.remove(tag)
	avaitag = tagiddomain[0]

	spcode = PaperRolldetails.objects.values_list('paper_code').distinct().order_by('paper_code')
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])

	swidth = PaperRolldetails.objects.values_list('size').distinct().order_by('size')
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	query = PaperRolldetails.objects.values_list('paper_roll_detail_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('rfid_roll_id','paper_roll_detail_id')

	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)

	for lst in nlist:
		roll_id = lst[0]
		if PaperMovement.objects.filter(roll_id=roll_id).exists() == True:
			current_weight = int(PaperMovement.objects.filter(roll_id=roll_id).order_by('-created_on')[0].actual_wt)
		else:
			current_weight = PaperRolldetails.objects.get(paper_roll_detail_id=roll_id).initial_weight
		lst.append(current_weight)

	if rfid_mode == 'real':
# Connect to RFID reader #
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			## soc.send('setup.operating_mode = standby\r\n')
			soc.send('tag.db.scan_tags(100)\r\n')
			datum = soc.recv(32)
			if datum.find("ok") > -1:
				soc.send('tag.read_id()\r\n')
				recv = soc.recv(8192)
				if recv.find("tag_id") > -1:
					cache.set('data', recv, 10) # Wait 10 seconds for 'data' to expire...
					timestamp = datetime.now().strftime("%H:%M:%S")
					cache.set('timestamp', timestamp, 10)
			soc.close()
		except:
			socror = 'Cannot connect to RFID reader'

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
					cnt = cnt+1

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
					cnt = cnt+1

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

			repeat_AA = list()

			for rep_A in repeat_A:
				repeat_AA.append(int(rep_A))

			if len(repeat_AA) > 0:
				if max(repeat_AA) in repeat_AA:
					n = repeat_AA.index(max(repeat_AA))
					realtag = tagid_A[n][7:11]
					tag2write = tagid_A[n][6:30]

					if tag2write.count('0') < 15 or PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.count('0') >= 15:
						tagstatus = 'known'

					if PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == True:
						rtquery = PaperRolldetails.objects.get(paper_roll_detail_id=realtag)
						paper_roll_id = rtquery.paper_roll_detail_id
						paper_code = rtquery.paper_code
						size = rtquery.size
						unit = rtquery.uom
						initial_weight = rtquery.initial_weight
						temp_weight = rtquery.temp_weight
						lane = rtquery.lane
						position = rtquery.position
						if position == None: position = ''

						if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
							actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
						else:
							actual_wt = rtquery.initial_weight

	if rfid_mode == 'fake':

#		atlocation = 'Scale'

#		atlane = 1
#		atposition = 4
#		atlocation = 'Stock'

		tag2write = '112233445566778899AABBCC'
		tag2write = '30065AAAA000000000000000'
		realtag = tag2write[1:5]

		lasttime = datetime.now().strftime("%H:%M:%S")

		if tag2write.count('0') < 15 or PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == False:
			tagstatus = 'unknown'
		elif tag2write.count('0') >= 15:
			tagstatus = 'known'

		if PaperRolldetails.objects.filter(paper_roll_detail_id=realtag).exists() == True:
			rtquery = PaperRolldetails.objects.get(paper_roll_detail_id=realtag)
			paper_roll_id = rtquery.paper_roll_detail_id
			paper_code = rtquery.paper_code
			size = rtquery.size
			unit = rtquery.uom
			initial_weight = rtquery.initial_weight
			temp_weight = rtquery.temp_weight
			lane = rtquery.lane
			position = rtquery.position

			if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
				actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
			else:
				actual_wt = rtquery.initial_weight

	return render_to_response('showtaglist.html', locals())

def createnew(request):
	if 'asupid' in request.GET and request.GET['asupid']:
		asupid = request.GET['asupid']

	if 'arollid' in request.GET and request.GET['arollid']:
		arollid = request.GET['arollid']

	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])
		if len(str(arfid)) == 1: strarfid = '000'+str(arfid)
		if len(str(arfid)) == 2: strarfid = '00'+str(arfid)
		if len(str(arfid)) == 3: strarfid = '0'+str(arfid)

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

#	if asupid and arollid and strarfid and apcode and asize and aweight and atag2write:
	if str(strarfid) == str(atag2write[1:5]):
		PaperRolldetails.objects.filter(paper_roll_detail_id=arollid).update(supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
	else:
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=3'+strarfid+'AAAA000000000000000, tag_id='+atag2write+', antenna=1 2)\r\n')
			response = soc.recv(128)
			soc.close()

			if response.find('ok') != -1:
				if atag2write.count('0') < 15:
					if PaperRolldetails.objects.filter(paper_roll_detail_id=arollid).exists() == False:
						PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=strarfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
					else:
						PaperRolldetails.objects.filter(paper_roll_detail_id=arollid).update(supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
				if atag2write.count('0') >= 15:
					PaperRolldetails.objects.create(paper_roll_detail_id=arollid, rfid_roll_id=strarfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
#						tag2del = int(atag2write[1:5])
#						PaperRolldetails.objects.filter(paper_roll_detail_id=tag2del).delete()
			else:
				mode = 'min'
				return HttpResponseRedirect('/django/tagman/')

		except socket.timeout:
			mode = 'min'
			socror = 'Cannot connect to RFID reader'
			return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')

def assigntag(request):
	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])
		if len(str(arfid)) == 1: strarfid = '000'+str(arfid)
		if len(str(arfid)) == 2: strarfid = '00'+str(arfid)
		if len(str(arfid)) == 3: strarfid = '0'+str(arfid)

#	if 'alane' in request.GET and request.GET['alane']:
#		alane = request.GET['alane']
#	else:
#		alane = ''

#	if 'aposition' in request.GET and request.GET['aposition']:
#		aposition = int(request.GET['aposition'])
#	else:
#		aposition = None

	if 'atag2write' in request.GET and request.GET['atag2write']:
		atag2write = request.GET['atag2write']

#	if strarfid and atag2write:
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=3'+strarfid+'AAAA000000000000000, tag_id='+atag2write+', antenna=1 2)\r\n')

		response = soc.recv(128)
		soc.close()

		if response.find('ok') != -1:
#			PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(rfid_roll_id=strarfid, lane=alane, position=aposition)
			PaperRolldetails.objects.filter(paper_roll_detail_id=arfid).update(rfid_roll_id=strarfid)
		else:
			mode = 'max'
			return render_to_response('writagror.html', locals())

	except socket.timeout:
		mode = 'max'
		socror = 'Cannot connect to RFID reader'
		return render_to_response('socror.html', locals())

	return render_to_response('totop.html')

def writemore(request):
	if 'arfid_more' in request.GET and request.GET['arfid_more']:
		arfid_more = int(request.GET['arfid_more'])
		if len(str(arfid_more)) == 1: strarfid_more = '000'+str(arfid_more)
		if len(str(arfid_more)) == 2: strarfid_more = '00'+str(arfid_more)
		if len(str(arfid_more)) == 3: strarfid_more = '0'+str(arfid_more)

	if 'atag2write_more' in request.GET and request.GET['atag2write_more']:
		atag2write_more = request.GET['atag2write_more']

#	if strarfid_more and atag2write_more:
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=3'+strarfid_more+'AAAA000000000000000, tag_id='+atag2write_more+', antenna=1 2)\r\n')

		response = soc.recv(128)
		soc.close()

		if response.find('ok') != -1:
			pass
		else:
			mode = 'max'
			return render_to_response('writagror.html', locals())

	except socket.timeout:
		mode = 'max'
		socror = 'Cannot connect to RFID reader'
		return render_to_response('socror.html', locals())

	return render_to_response('totop.html')

def loctag(request):
	if 'alane_loc' in request.GET and request.GET['alane_loc']:
		alane_loc = request.GET['alane_loc']
		if alane_loc == '1': letalane_loc = 'AB'
		if alane_loc == '2': letalane_loc = 'CD'
		if alane_loc == '3': letalane_loc = 'EF'
		if alane_loc == '4': letalane_loc = 'FF'
		if alane_loc == 'CR': letalane_loc = 'CC'
		if alane_loc == 'Scale': letalane_loc = 'DD'
	else:
		alane_loc = ''

	if 'aposition_loc' in request.GET and request.GET['aposition_loc']:
		aposition_loc = int(request.GET['aposition_loc'])
		if len(str(aposition_loc)) == 1: straposition_loc = '00'+str(aposition_loc)
		if len(str(aposition_loc)) == 2: straposition_loc = '0'+str(aposition_loc)
	else:
		aposition_loc = None

	if 'atag2write_loc' in request.GET and request.GET['atag2write_loc']:
		atag2write_loc = request.GET['atag2write_loc']

#	if alane_loc and aposition_loc and atag2write_loc:
	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=3BBBB00000000000000'+letalane_loc+straposition_loc+', tag_id='+atag2write_loc+', antenna=1 2)\r\n')

		response = soc.recv(128)
		soc.close()

		if response.find('ok') != -1:
			pass
		else:
			mode = 'min'
			return render_to_response('writagror.html', locals())

	except socket.timeout:
		mode = 'min'
		socror = 'Cannot connect to RFID reader'
		return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')
