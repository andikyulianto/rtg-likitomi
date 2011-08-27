from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.cache import cache
from datetime import datetime

import socket

from weight.models import PaperRolldetails, PaperMovement

# HOST and PORT settings for RFID reader connection
HOST = '192.168.2.88' # Likitomi's factory
PORT = 50007

rfid_mode = 'real' # RFID mode = {'real', 'fake'}

def tagman(request):
	"""
	Manage RFID tag including both paper roll ID tags and location tags.

		Write an RFID tag for a particular paper roll.

		Write an RFID tag for a particular location.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

		:model:`weight.PaperMovement`

	``Special Modules``

		socket: For making a connection to RFID reader.

	**Template:**

	:template:`templates/clamplift/tagman.html`

	"""

	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('likitomi_roll_id')
	tagidlist = PaperRolldetails.objects.values_list('likitomi_roll_id', flat=True).order_by('-likitomi_roll_id')
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

	query = PaperRolldetails.objects.values_list('likitomi_roll_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('-likitomi_roll_id')

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
			current_weight = PaperRolldetails.objects.get(likitomi_roll_id=roll_id).initial_weight
		lst.append(current_weight)

# Connect to RFID reader #
	if rfid_mode == 'real':
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
					cache.set('timestamp', timestamp, 10) # Wait 10 seconds for 'timestamp' to expire...
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
				if "3000000000000000000" in tag: # Pattern of location tag
					loclist.append(tag)
				else: # This will append both paper roll ID tag and new (unknown) tag into "idlist"
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

			cnt_sum = len(tagid_A) + len(tagid_B)
			lan = 0
			pos = 0
			totalCount = 0

			if len(repeat_B) > 0 :
				cnt = 0
				for rep in repeat_B:
					if type_B[cnt] == "ISOC":
						prelindex = tagid_B[cnt][21:23]
						if prelindex == 'AB': lindex = 1
						if prelindex == 'CD': lindex = 2
						if prelindex == 'EF': lindex = 3
						if prelindex == 'FF': lindex = 4
						if prelindex == 'CC': lindex = 0
						if prelindex == 'DD': lindex = 5
						pindex = int(tagid_B[cnt][23:26])
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
					realtag = tagid_A[n][16:30]
					tag2write = tagid_A[n][2:30]

					if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.find('30000000000000') == 0:
						tagstatus = 'known'

					if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
						rtquery = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
						likitomi_roll_id = rtquery.likitomi_roll_id
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

	if rfid_mode == 'fake': # Fake mode just for running application without weighing indicator

#		atlocation = 'Scale'

#		atlane = 1
#		atposition = 4
#		atlocation = 'Stock'

		tag2write = '112233445566778899AABBCC'
#		tag2write = '300000000000005408090065'
		realtag = tag2write[14:24]

		lasttime = datetime.now().strftime("%H:%M:%S")

		if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
			tagstatus = 'unknown'
		elif tag2write.find('30000000000000') == 0:
			tagstatus = 'known'

		if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
			rtquery = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
			likitomi_roll_id = rtquery.likitomi_roll_id
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
	"""
	Manage RFID tag including both paper roll ID tags and location tags.

		Write an RFID tag for a particular paper roll.

		Write an RFID tag for a particular location.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

		:model:`weight.PaperMovement`

	``Special Modules``

		socket: For making a connection to RFID reader.

	**Template:**

	:template:`templates/clamplift/tagman.html`

	"""

	tagiddomain = range(1,10000)
	tagidquery = PaperRolldetails.objects.values_list('likitomi_roll_id')
	tagidlist = PaperRolldetails.objects.values_list('likitomi_roll_id', flat=True).order_by('-likitomi_roll_id')
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

	query = PaperRolldetails.objects.values_list('likitomi_roll_id', 'rfid_roll_id', 'paper_code', 'size', 'initial_weight', 'lane', 'position').order_by('-likitomi_roll_id')

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
			current_weight = PaperRolldetails.objects.get(likitomi_roll_id=roll_id).initial_weight
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
					cache.set('timestamp', timestamp, 10) # Wait 10 seconds for 'timestamp' to expire...
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
				if "3000000000000000000" in tag: # Pattern of location tag
					loclist.append(tag)
				else: # This will append both paper roll ID tag and new (unknown) tag into "idlist"
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
						prelindex = tagid_B[cnt][21:23]
						if prelindex == 'AB': lindex = 1
						if prelindex == 'CD': lindex = 2
						if prelindex == 'EF': lindex = 3
						if prelindex == 'FF': lindex = 4
						if prelindex == 'CC': lindex = 0
						if prelindex == 'DD': lindex = 5
						pindex = int(tagid_B[cnt][23:26])
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
					realtag = tagid_A[n][16:30]
					tag2write = tagid_A[n][2:30]

					if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
						tagstatus = 'unknown'
					elif tag2write.find('30000000000000') == 0:
						tagstatus = 'known'

					if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
						rtquery = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
						likitomi_roll_id = rtquery.likitomi_roll_id
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
		tag2write = '300000000000005408090065'
		realtag = tag2write[14:24]

		lasttime = datetime.now().strftime("%H:%M:%S")

		if tag2write.find('30000000000000') == -1 or PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == False:
			tagstatus = 'unknown'
		elif tag2write.find('30000000000000') == 0:
			tagstatus = 'known'

		if realtag and PaperRolldetails.objects.filter(likitomi_roll_id=realtag).exists() == True:
			rtquery = PaperRolldetails.objects.get(likitomi_roll_id=realtag)
			likitomi_roll_id = rtquery.likitomi_roll_id
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

	if str(arfid) == str(atag2write[1:5]):
		PaperRolldetails.objects.filter(likitomi_roll_id=arollid).update(supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
	else:
		try:
			soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			soc.settimeout(2)
			soc.connect((HOST, PORT))
			soc.send('tag.write_id(new_tag_id=30000000000000'+str(arfid)+', tag_id='+atag2write+', antenna=2 3)\r\n')
			response = soc.recv(128)
			soc.close()

			if response.find('ok') != -1:
				if atag2write.find('30000000000000') == -1:
					if PaperRolldetails.objects.filter(likitomi_roll_id=arollid).exists() == False:
						PaperRolldetails.objects.create(likitomi_roll_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
					else:
						PaperRolldetails.objects.filter(likitomi_roll_id=arollid).update(supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
				if atag2write.find('30000000000000') == 0:
					PaperRolldetails.objects.create(likitomi_roll_id=arollid, rfid_roll_id=arfid, supplier_roll_id=asupid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
			else:
				mode = 'min'
				return HttpResponseRedirect('/django/tagman/')

		except socket.timeout:
			mode = 'min'
			socror = 'Cannot connect to RFID reader'
			return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/tagman/')

def assigntag(request):
	"""
	Assign RFID tag to a new paper roll ID.

		Write an RFID tag for a particular paper roll using Likitomi roll ID.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

	``Special Modules``

		socket: For making a connection to RFID reader.

	"""

	if 'arfid' in request.GET and request.GET['arfid']:
		arfid = int(request.GET['arfid'])

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

	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=30000000000000'+str(arfid)+', tag_id='+atag2write+', antenna=2 3)\r\n')

		response = soc.recv(128)
		soc.close()

		if response.find('ok') != -1:
#			PaperRolldetails.objects.filter(likitomi_roll_id=arfid).update(rfid_roll_id=arfid, lane=alane, position=aposition)
			PaperRolldetails.objects.filter(likitomi_roll_id=arfid).update(rfid_roll_id=arfid)
		else:
			mode = 'max'
			return render_to_response('writagror.html', locals())

	except socket.timeout:
		mode = 'max'
		socror = 'Cannot connect to RFID reader'
		return render_to_response('socror.html', locals())

	return render_to_response('totop.html')

def writemore(request):
	"""
	Assign RFID tag to an existing paper roll ID.

		Write an RFID tag for a particular paper roll using Likitomi roll ID.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

	``Special Modules``

		socket: For making a connection to RFID reader.

	"""

	if 'arfid_more' in request.GET and request.GET['arfid_more']:
		arfid_more = int(request.GET['arfid_more'])

	if 'atag2write_more' in request.GET and request.GET['atag2write_more']:
		atag2write_more = request.GET['atag2write_more']

	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=30000000000000'+str(arfid_more)+', tag_id='+atag2write_more+', antenna=2 3)\r\n')

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
	"""
	Assign RFID tag to a location.

		Write an RFID tag for a particular location by specifying lane and position.

	**Context:**

	``Special Modules``

		socket: For making a connection to RFID reader.

	"""

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

	try:
		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		soc.settimeout(2)
		soc.connect((HOST, PORT))
		soc.send('tag.write_id(new_tag_id=3000000000000000000'+letalane_loc+straposition_loc+', tag_id='+atag2write_loc+', antenna=2 3)\r\n')

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

