# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan, PaperRoll, PaperHistory

import socket

def minclamp(request):
	try:
# RFID: paper roll and location tags #
		operating_mode = 'fake' # Operating mode = {'real', 'fake'}

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
				data = soc.recv(8192)
				tagdata = data.split("\r\n")

			idlist = list()
			loclist = list()

			for tag in tagdata:
#				if "AAAA" in tag:
#					idlist.append(tag)
#				if "BBBB" in tag:
#					loclist.append(tag)
				if "type=STG" in tag or "AAAA" in tag:
					idlist.append(tag)
				if "type=ISOC" and "AAAA" not in tag or "BBBB" in tag:
					loclist.append(tag)

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

			soc.close()

		if operating_mode == 'fake':

#			atlane = 5
#			atposition = 5
#			atlocation = 'Scale'

			atlane = '2'
			atposition = '2'
			atlocation = 'Stock'

			realtag = 67

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

#			uppos = int(position)+1
#			downpos = int(position)-1
#			if lane == 'A': opplane = 'B'
#			if lane == 'B': opplane = 'A' 
#			if lane == 'C': opplane = 'D'
#			if lane == 'D': opplane = 'C'
#			if lane == 'E': opplane = 'F'
#			if lane == 'F': opplane = 'E'
#			if lane == 'G': opplane = 'H'
#			if lane == 'H': opplane = 'G'

#			if atlane == '1':
#				leftlane = 'A'
#				rightlane = 'B'
#			if atlane == '2':
#				leftlane = 'C'
#				rightlane = 'D'
#			if atlane == '3':
#				leftlane = 'E'
#				rightlane = 'F'
#			if atlane == '4':
#				leftlane = 'G'
#				rightlane = 'H'

# For Hulk #
#			digital = str(temp_weight)
#			if len(digital) == 7:
#				digit1 = digital[0:1]
#				digit2 = digital[1:2]
#				digit3 = digital[2:3]
#				digit4 = digital[3:4]
#				digit5 = digital[4:5]
#				digit6 = digital[5:6]
#				digit7 = digital[6:7]
#			if len(digital) == 6:
#				digit2 = digital[0:1]
#				digit3 = digital[1:2]
#				digit4 = digital[2:3]
#				digit5 = digital[3:4]
#				digit6 = digital[4:5]
#				digit7 = digital[5:6]
#			if len(digital) == 5:
#				digit3 = digital[0:1]
#				digit4 = digital[1:2]
#				digit5 = digital[2:3]
#				digit6 = digital[3:4]
#				digit7 = digital[4:5]
#			if len(digital) == 4:
#				digit4 = digital[0:1]
#				digit5 = digital[1:2]
#				digit6 = digital[2:3]
#				digit7 = digital[3:4]

#			if len(digital) == 3:
#				digit5 = digital[0:1]
#				digit6 = digital[1:2]
#				digit7 = digital[2:3]

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
		return HttpResponseRedirect('/minclamp/')

	if 'temp_weight' in request.GET and request.GET['temp_weight']:
		temp_weight = request.GET['temp_weight']
	else:
		return HttpResponseRedirect('/minclamp/')

	if 'actual_wt' in request.GET and request.GET['actual_wt']:
		actual_wt = request.GET['actual_wt']
	else:
		return HttpResponseRedirect('/minclamp/')

	p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=temp_weight)
	p.save()
	transaction.commit()

	return HttpResponseRedirect('/minclamp/')

### UNDO ###
@transaction.commit_manually
def minundo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/minclamp/')

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()
	transaction.commit()

#	transaction.rollback()

	return HttpResponseRedirect('/minclamp/')

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

	return HttpResponseRedirect('/minclamp/')

def maxclamp(request):
	try:
# RFID: paper roll and location tags #
		operating_mode = 'fake' # Operating mode = {'real', 'fake'}

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
				data = soc.recv(8192)
				tagdata = data.split("\r\n")

			idlist = list()
			loclist = list()

			for tag in tagdata:
#				if "AAAA" in tag:
#					idlist.append(tag)
#				if "BBBB" in tag:
#					loclist.append(tag)
				if "type=STG" in tag or "AAAA" in tag:
					idlist.append(tag)
				if "type=ISOC" and "AAAA" not in tag or "BBBB" in tag:
					loclist.append(tag)

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

			soc.close()

		if operating_mode == 'fake':

#			atlane = 5
#			atposition = 5
#			atlocation = 'Scale'

			atlane = '2'
			atposition = '2'
			atlocation = 'Stock'

			realtag = 67

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

#			uppos = int(position)+1
#			downpos = int(position)-1
#			if lane == 'A': opplane = 'B'
#			if lane == 'B': opplane = 'A' 
#			if lane == 'C': opplane = 'D'
#			if lane == 'D': opplane = 'C'
#			if lane == 'E': opplane = 'F'
#			if lane == 'F': opplane = 'E'
#			if lane == 'G': opplane = 'H'
#			if lane == 'H': opplane = 'G'

#			if atlane == '1':
#				leftlane = 'A'
#				rightlane = 'B'
#			if atlane == '2':
#				leftlane = 'C'
#				rightlane = 'D'
#			if atlane == '3':
#				leftlane = 'E'
#				rightlane = 'F'
#			if atlane == '4':
#				leftlane = 'G'
#				rightlane = 'H'

# For Hulk #
#			digital = str(temp_weight)
#			if len(digital) == 7:
#				digit1 = digital[0:1]
#				digit2 = digital[1:2]
#				digit3 = digital[2:3]
#				digit4 = digital[3:4]
#				digit5 = digital[4:5]
#				digit6 = digital[5:6]
#				digit7 = digital[6:7]
#			if len(digital) == 6:
#				digit2 = digital[0:1]
#				digit3 = digital[1:2]
#				digit4 = digital[2:3]
#				digit5 = digital[3:4]
#				digit6 = digital[4:5]
#				digit7 = digital[5:6]
#			if len(digital) == 5:
#				digit3 = digital[0:1]
#				digit4 = digital[1:2]
#				digit5 = digital[2:3]
#				digit6 = digital[3:4]
#				digit7 = digital[4:5]
#			if len(digital) == 4:
#				digit4 = digital[0:1]
#				digit5 = digital[1:2]
#				digit6 = digital[2:3]
#				digit7 = digital[3:4]

#			if len(digital) == 3:
#				digit5 = digital[0:1]
#				digit6 = digital[1:2]
#				digit7 = digital[2:3]

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

	return render_to_response('maxclamp.html', locals())

### UPDATE ###
@transaction.commit_manually
def maxupdate(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/maxclamp/')

	if 'temp_weight' in request.GET and request.GET['temp_weight']:
		temp_weight = request.GET['temp_weight']
	else:
		return HttpResponseRedirect('/maxclamp/')

	if 'actual_wt' in request.GET and request.GET['actual_wt']:
		actual_wt = request.GET['actual_wt']
	else:
		return HttpResponseRedirect('/maxclamp/')

	p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=temp_weight)
	p.save()
	transaction.commit()

	return HttpResponseRedirect('/maxclamp/')

### UNDO ###
@transaction.commit_manually
def maxundo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/maxclamp/')

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()
	transaction.commit()

#	transaction.rollback()

	return HttpResponseRedirect('/maxclamp/')

def maxchangeloc(request):
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

	return HttpResponseRedirect('/maxclamp/')
