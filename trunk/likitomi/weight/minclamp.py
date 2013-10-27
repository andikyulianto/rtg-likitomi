from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.cache import cache
from datetime import datetime

import socket

from weight.models import PaperRolldetails, PaperMovement, TempWeight

# HOST and PORT settings for RFID reader connection
HOST = '192.168.2.88' # Likitomi's factory
PORT = 50007

rfid_mode = 'real' # RFID mode = {'real', 'fake'}

def minclamp(request):
	"""
	Displays the information of the current paper roll on clamp-lift vehicle with updating weight and location functions.

		Connect and retrieve the paper roll tag information from RFID reader.

		Display the information of the current paper roll on the clamp-lift vehicle including Likitomi roll ID, paper code, size, location, and weight.

		Provide the function to update the weight when the clamp-lift vehicle is at scale.

		Provide the function to update the location when the clamp-lift vehicle is in paper roll stock area.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

		:model:`weight.PaperMovement`

	``Special Modules``

		socket: For making a connection to RFID reader.

	**Template:**

	:template:`templates/clamplift/minclamp.html`

	"""

	if 'clampsta' in request.GET and request.GET['clampsta']:
		clampsta = request.GET['clampsta']

# Query tag ID, paper code, and size for assigning tag
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

# Connect to RFID reader
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
						paper_roll_id = rtquery.likitomi_roll_id
						paper_code = rtquery.paper_code
						size = rtquery.size
						unit = rtquery.uom
						initial_weight = rtquery.initial_weight
#						temp_weight = rtquery.temp_weight
						lane = rtquery.lane
						position = rtquery.position
						if position == None: position = ''

						if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
							actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
						else:
							actual_wt = rtquery.initial_weight
							undo_btn = ""

		temp_weight = int(TempWeight.objects.order_by('-timestamp')[0].weight)

	if rfid_mode == 'fake': # Fake mode just for running application without weighing indicator

#		atlocation = 'Scale'

		atlane = 1
		atposition = 33
		atlocation = 'Stock'

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
			paper_roll_id = rtquery.likitomi_roll_id
			paper_code = rtquery.paper_code
			size = rtquery.size
			unit = rtquery.uom
			initial_weight = rtquery.initial_weight
#			temp_weight = rtquery.temp_weight
			lane = rtquery.lane
			position = rtquery.position

			if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
				actual_wt = int(PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0].actual_wt)
			else:
				actual_wt = rtquery.initial_weight
				undo_btn = ""

		temp_weight = int(TempWeight.objects.order_by('-timestamp')[0].weight)

	return render_to_response('minclamp.html', locals())

### UPDATE ###
def minupdate(request):
	"""
	Update function for changing the weight of paper roll to the latest one from weighing indicator or manual input.

		Add the record of changing weight of paper roll to :model:`weight.PaperMovement`.

	**Context:**

	``Models``

		:model:`weight.PaperMovement`

	"""

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	if 'temp_weight' in request.GET and request.GET['temp_weight']:
		temp_weight = request.GET['temp_weight']

	if 'actual_wt' in request.GET and request.GET['actual_wt']:
		actual_wt = request.GET['actual_wt']

	if 'clampsta' in request.GET and request.GET['clampsta']:
		clampsta = request.GET['clampsta']

	now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	p = PaperMovement(roll_id=realtag, before_wt=actual_wt, actual_wt=temp_weight, created_on=now)
	p.save()

	return HttpResponseRedirect('/django/minclamp/?clampsta='+clampsta)

### UNDO ###
def minundo(request):
	"""
	Undo function for rolling back the weight of paper roll to the previous one.

		Delete the record of changing weight of paper roll in :model:`weight.PaperMovement`.

	**Context:**

	``Models``

		:model:`weight.PaperMovement`

	"""

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	if 'clampsta' in request.GET and request.GET['clampsta']:
		clampsta = request.GET['clampsta']

	if PaperMovement.objects.filter(roll_id=realtag).exists() == True:
		p = PaperMovement.objects.filter(roll_id=realtag).order_by('-created_on')[0]
		p.delete()

	return HttpResponseRedirect('/django/minclamp/?clampsta='+clampsta)

### CHANGE LOC ###
def minchangeloc(request):
	"""
	Changing location function for changing location directly on the map or by manually input.

		Change the values of lane and position of the paper roll in :model:`weight.PaperRolldetails`.

	**Context:**

	``Models``

		:model:`weight.PaperRolldetails`

	"""

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']

	if 'lane' in request.GET and request.GET['lane']:
		ilane = request.GET['lane']

	if 'pos' in request.GET and request.GET['pos']:
		ipos = request.GET['pos']

	if 'clampsta' in request.GET and request.GET['clampsta']:
		clampsta = request.GET['clampsta']

	PaperRolldetails.objects.filter(likitomi_roll_id=realtag).update(lane=ilane, position=ipos)

	return HttpResponseRedirect('/django/minclamp/?clampsta='+clampsta)


def minassigntag(request):
	if 'atagid' in request.GET and request.GET['atagid']:
		atagid = int(request.GET['atagid'])

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

	if atagid and apcode and asize and aweight and atag2write:
		if str(atagid) == str(atag2write[20:30]):
			PaperRolldetails.objects.filter(likitomi_roll_id=atagid).update(paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
		else:
			try:
				soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				soc.settimeout(2)
				soc.connect((HOST, PORT))
				soc.send('tag.write_id(new_tag_id=30000000000000'+str(atagid)+', tag_id='+atag2write+', antenna=2 3)\r\n')
				response = soc.recv(128)
				soc.close()

				if response.find('ok') != -1:
					if atag2write.find('30000000000000') == -1:
						PaperRolldetails.objects.create(likitomi_roll_id=atagid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
					if atag2write.find('30000000000000') == 0:
						PaperRolldetails.objects.create(likitomi_roll_id=atagid, paper_code=apcode, size=asize, uom='inch', initial_weight=aweight, lane=alane, position=aposition)
						tag2del = int(atag2write[20:30])
						PaperRolldetails.objects.filter(likitomi_roll_id=tag2del).delete()
				else:
					mode = 'min'
					return render_to_response('writagror.html', locals())

			except socket.timeout:
				mode = 'min'
				socror = 'Cannot connect to RFID reader'
				return render_to_response('socror.html', locals())

	return HttpResponseRedirect('/django/minclamp/')

