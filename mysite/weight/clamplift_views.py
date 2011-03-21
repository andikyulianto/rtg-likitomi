# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from mysite.weight.models import ClampliftPlan, PaperRoll, PaperHistory

import socket

def clamplift(request):
# Connect RFID reader #
	try:
		operating_mode = 'fake' # Operating mode = {'real', 'fake'} #

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
			soc.send('tag.db.scan_tags(1000)\r\n')
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
			real = tagid_A[0]
			realtag = tagid_A[n][7:11]

			soc.close()

		if operating_mode == 'fake':

#			atlane = '5'
#			atposition = '5'
#			atlocation = 'Scale'

			atlane = '1'
			atposition = '5'
			atlocation = 'Stock'

			realtag = 67

# Query database #
		query = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'width', 'initial_weight','temp_weight', 'lane', 'position')[0]
		query1 = list(query)

		paper_roll_id = query1[0]
		paper_code = query1[1]
		size = query1[2]
		initial_weight = query1[3]
		temp_weight = query1[4]
		lane = query1[5]
		position = query1[6]
		uppos = int(position)+1
		downpos = int(position)-1
		digital = str(temp_weight)+".0"
		lend = len(digital)

		if lane == 'A':
			opplane = 'B'
		if lane == 'B':
			opplane = 'A' 
		if lane == 'C':
			opplane = 'D' 
		if lane == 'D':
			opplane = 'C' 
		if lane == 'E':
			opplane = 'F' 
		if lane == 'F':
			opplane = 'E' 
		if lane == 'G':
			opplane = 'H'
		if lane == 'H':
			opplane = 'G' 

		if atlane == '1':
			leftlane = 'A'
			rightlane = 'B'
		if atlane == '2':
			leftlane = 'C'
			rightlane = 'D'
		if atlane == '3':
			leftlane = 'E'
			rightlane = 'F'
		if atlane == '4':
			leftlane = 'G'
			rightlane = 'H'

		if atlocation != 'Scale':
			wgth_dis = ""
			man_btn = ""
			undo_btn = ""
			submit_btn = ""
			digital = ""

		if len(digital) == 7:
			digit1 = digital[0:1]
			digit2 = digital[1:2]
			digit3 = digital[2:3]
			digit4 = digital[3:4]
			digit5 = digital[4:5]
			digit6 = digital[5:6]
			digit7 = digital[6:7]
		if len(digital) == 6:
			digit2 = digital[0:1]
			digit3 = digital[1:2]
			digit4 = digital[2:3]
			digit5 = digital[3:4]
			digit6 = digital[4:5]
			digit7 = digital[5:6]
		if len(digital) == 5:
			digit3 = digital[0:1]
			digit4 = digital[1:2]
			digit5 = digital[2:3]
			digit6 = digital[3:4]
			digit7 = digital[4:5]
		if len(digital) == 4:
			digit4 = digital[0:1]
			digit5 = digital[1:2]
			digit6 = digital[2:3]
			digit7 = digital[3:4]
		if len(digital) == 3:
			digit5 = digital[0:1]
			digit6 = digital[1:2]
			digit7 = digital[2:3]

		query222 = PaperHistory.objects.filter(roll_id=realtag).exists()

		if query222 == True:
			query22 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
			query2 = list(query22)
			actual_wt = query2[0]
		else:
			actual_wt = initial_weight
			undo_btn = ""

		availoc = ['1A','1B','1C','1D','1E']
		availoc = availoc + ['2A','2B','2C','2D','2E']
		availoc = availoc + ['3A','3B','3C','3D','3E','3F','3G','3H']
		availoc = availoc + ['4A','4B','4C','4D','4E','4F','4G','4H']
		availoc = availoc + ['5A','5B','5C','5D','5E','5F','5G','5H']
		availoc = availoc + ['6A','6B','6C','6D','6E','6F','6G','6H']
		availoc = availoc + ['7A']
		availoc = availoc + ['8A','8B','8C','8D','8E','8F','8G','8H']
		availoc = availoc + ['9A','9B','9C','9D','9E','9F','9G','9H']
		availoc = availoc + ['10A','10B','10C']
		availoc = availoc + ['11A','11B','11C']
		availoc = availoc + ['12A','12B','12C']
		availoc = availoc + ['13A','13B','13C']

# Exceptions #
	except UnboundLocalError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Please change operating mode to 'standby'.]"
		return render_to_response('clamplift.html', locals())

	except ValueError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		return render_to_response('clamplift.html', locals())

	except TypeError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		return render_to_response('clamplift.html', locals())

	except: # Timeout #
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Cannot connect RFID reader before timeout.]"
		return render_to_response('clamplift.html', locals())

	return render_to_response('clamplift.html', locals())

###################################################################### UPDATE ######################################################################

@transaction.commit_manually
def update(request):
	if 'weight' in request.GET and request.GET['weight']:
		weight = request.GET['weight']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	query11 = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'initial_weight', 'width', 'wunit', 'temp_weight')[0]
	query1 = list(query11)

	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[2]
	size = query1[3]
	uom = query1[4]
	temp_weight = query1[5]

	query222 = PaperHistory.objects.filter(roll_id=realtag).exists()

	if query222 == True:
		query22 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
		query2 = list(query22)
		actual_wt = query2[0]
	else:
		actual_wt = initial_weight
		undo_btn = ""

	int_weight = int(weight)

	try:
		f_weight = float(weight)
	except ValueError:
		error = "Your submitted weight is not a number."
		return render_to_response('submit_error.html', locals())

	if actual_wt > f_weight:
		p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=int_weight)
		p.save()
		transaction.commit()

	else:
		err = "w"
		error = "Your submitted weight is not less than previous weight."
		return render_to_response('submit_error.html', locals())

	return HttpResponseRedirect('/clamplift/')

###################################################################### UNDO ######################################################################

def undo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	query11 = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'initial_weight', 'width', 'wunit', 'temp_weight')[0]
	query1 = list(query11)

	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[2]
	size = query1[3]
	uom = query1[4]
	temp_weight = query1[5]

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()
	transaction.commit()

#	transaction.rollback()

	return HttpResponseRedirect('/clamplift/')

################################################################## CHANGE LOCATION #################################################################

def changeloc(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'lane' in request.GET and request.GET['lane']:
		ilane = request.GET['lane']
	else:
		return HttpResponseRedirect('/clamplift/')

	if 'pos' in request.GET and request.GET['pos']:
		ipos = request.GET['pos']
	else:
		return HttpResponseRedirect('/clamplift/')

	availoc = ['1A','1B','1C']
	availoc = availoc + ['2A','2B','2C']
	availoc = availoc + ['3A','3B','3C','3D','3E','3F','3G','3H']
	availoc = availoc + ['4A','4B','4C','4D','4E','4F','4G','4H']
	availoc = availoc + ['5A','5B','5C','5D','5E','5F','5G','5H']
	availoc = availoc + ['6A','6B','6C','6D','6E','6F','6G','6H']
	availoc = availoc + ['7A']
	availoc = availoc + ['8A','8B','8C','8D','8E','8F','8G','8H']
	availoc = availoc + ['9A','9B','9C','9D','9E','9F','9G','9H']
	availoc = availoc + ['10A','10B','10C']
	availoc = availoc + ['11A','11B','11C']
	availoc = availoc + ['12A','12B','12C']
	availoc = availoc + ['13A','13B','13C']

	iposlane = str(ipos) + ilane
	if iposlane in availoc:
		query = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'temp_weight')[0]
		qlist = list(query)
		paper_code = qlist[0]
		width = qlist[1]
		wunit = qlist[2]
		initial_weight = qlist[3]
		temp_weight = qlist[4]
		p = PaperRoll(id=realtag, width=width, wunit=wunit, initial_weight=initial_weight, temp_weight=temp_weight)
		p.paper_code = paper_code
		p.width = width
		p.wunit = wunit
		p.initial_weight = initial_weight
		p.temp_weight = temp_weight
		p.lane = ilane
		p.position = ipos
		p.save()

	else:
		err = ""
		error = "Your submitted location is not available in the map."
		return render_to_response('submit_error.html', locals())

	return HttpResponseRedirect('/clamplift/')

################################################################## REPEAT #################################################################
################################################################## REPEAT #################################################################

def minclamp(request):
# Connect RFID reader #
	try:
		operating_mode = 'fake' # Operating mode = {'real', 'fake'} #

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

			atlane = '1'
			atposition = '5'
			atlocation = 'Stock'

			realtag = 67

# Query database #
		query = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'width', 'initial_weight','temp_weight', 'lane', 'position')[0]
		query1 = list(query)

		paper_roll_id = query1[0]
		paper_code = query1[1]
		size = query1[2]
		initial_weight = query1[3]
		temp_weight = query1[4]
		lane = query1[5]
		position = query1[6]
		uppos = int(position)+1
		downpos = int(position)-1
		digital = str(temp_weight)

		if lane == 'A':
			opplane = 'B'
		if lane == 'B':
			opplane = 'A' 
		if lane == 'C':
			opplane = 'D'
		if lane == 'D':
			opplane = 'C'
		if lane == 'E':
			opplane = 'F'
		if lane == 'F':
			opplane = 'E'
		if lane == 'G':
			opplane = 'H'
		if lane == 'H':
			opplane = 'G'

		if atlane == '1':
			leftlane = 'A'
			rightlane = 'B'
		if atlane == '2':
			leftlane = 'C'
			rightlane = 'D'
		if atlane == '3':
			leftlane = 'E'
			rightlane = 'F'
		if atlane == '4':
			leftlane = 'G'
			rightlane = 'H'

		if atlocation != 'Scale':
			wgth_dis = ""
			man_btn = ""
			undo_btn = ""
			submit_btn = ""
			digital = ""

		if len(digital) == 7:
			digit1 = digital[0:1]
			digit2 = digital[1:2]
			digit3 = digital[2:3]
			digit4 = digital[3:4]
			digit5 = digital[4:5]
			digit6 = digital[5:6]
			digit7 = digital[6:7]
		if len(digital) == 6:
			digit2 = digital[0:1]
			digit3 = digital[1:2]
			digit4 = digital[2:3]
			digit5 = digital[3:4]
			digit6 = digital[4:5]
			digit7 = digital[5:6]
		if len(digital) == 5:
			digit3 = digital[0:1]
			digit4 = digital[1:2]
			digit5 = digital[2:3]
			digit6 = digital[3:4]
			digit7 = digital[4:5]
		if len(digital) == 4:
			digit4 = digital[0:1]
			digit5 = digital[1:2]
			digit6 = digital[2:3]
			digit7 = digital[3:4]

		if len(digital) == 3:
			digit5 = digital[0:1]
			digit6 = digital[1:2]
			digit7 = digital[2:3]

		query222 = PaperHistory.objects.filter(roll_id=realtag).exists()

		if query222 == True:
			query22 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
			query2 = list(query22)
			actual_wt = query2[0]
		else:
			actual_wt = initial_weight
			undo_btn = ""

# Exceptions #
	except UnboundLocalError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Please change operating mode to 'standby'.]"
		digital = ""
		return render_to_response('minclamp.html', locals())

	except ValueError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		digital = ""
		return render_to_response('minclamp.html', locals())

	except TypeError:
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
#		atlane = ""
#		atposition = ""
#		atlocation = ""
		actual_wt = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[No ID tag in field.]"
		digital = ""
		return render_to_response('minclamp.html', locals())

	except: # Timeout #
		realtag = ""
		paper_code = ""
		size = ""
		lane = ""
		position = ""
		atlane = ""
		atposition = ""
		atlocation = ""
		actual_wt = ""
		used_weight = ""
		wgth_dis = ""
		man_btn = ""
		undo_btn = ""
		submit_btn = ""
		bottomerror = "[Cannot connect RFID reader before timeout.]"
		digital = ""
		return render_to_response('minclamp.html', locals())

	return render_to_response('minclamp.html', locals())

###################################################################### UPDATE ######################################################################

@transaction.commit_manually
def minupdate(request):
	if 'weight' in request.GET and request.GET['weight']:
		weight = request.GET['weight']
	else:
		return HttpResponseRedirect('/minclamp/')

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/minclamp/')

	query11 = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'initial_weight', 'width', 'wunit', 'temp_weight')[0]
	query1 = list(query11)

	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[2]
	size = query1[3]
	uom = query1[4]
	temp_weight = query1[5]

	query222 = PaperHistory.objects.filter(roll_id=realtag).exists()

	if query222 == True:
		query22 = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp').values_list('last_wt')[0]
		query2 = list(query22)
		actual_wt = query2[0]
	else:
		actual_wt = initial_weight
		undo_btn = ""

	int_weight = int(weight)

	try:
		f_weight = float(weight)
	except ValueError:
		error = "Your submitted weight is not a number."
		return render_to_response('submit_error_min.html', locals())

	if actual_wt > f_weight:
		p = PaperHistory(roll_id=realtag, before_wt=actual_wt, last_wt=int_weight)
		p.save()
		transaction.commit()

	else:
		err = "w"
		error = "Your submitted weight is not less than previous weight."
		return render_to_response('submit_error_min.html', locals())

	return HttpResponseRedirect('/minclamp/')

###################################################################### UNDO ######################################################################

@transaction.commit_manually
def minundo(request):
	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		return HttpResponseRedirect('/minclamp/')

	query11 = PaperRoll.objects.filter(id=realtag).values_list('id', 'paper_code', 'initial_weight', 'width', 'wunit', 'temp_weight')[0]
	query1 = list(query11)

	paper_roll_id = query1[0]
	paper_code = query1[1]
	initial_weight = query1[2]
	size = query1[3]
	uom = query1[4]
	temp_weight = query1[5]

	p = PaperHistory.objects.filter(roll_id=realtag).order_by('-timestamp')[0]
	p.delete()
	transaction.commit()

#	transaction.rollback()

	return HttpResponseRedirect('/minclamp/')

################################################################## CHANGE LOCATION #################################################################

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

	if 'pcode' in request.GET and request.GET['pcode']:
		ipcode = request.GET['pcode']
	else:
		ipcode = ""

	if 'width' in request.GET and request.GET['width']:
		iwidth = request.GET['width']
	else:
		iwidth = ""

	if 'loss' in request.GET and request.GET['loss']:
		iloss = request.GET['loss']
	else:
		iloss = ""

	if int(ipos) <= 43:
		query = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'temp_weight')[0]
		qlist = list(query)
		paper_code = qlist[0]
		width = qlist[1]
		wunit = qlist[2]
		initial_weight = qlist[3]
		temp_weight = qlist[4]
		p = PaperRoll(id=realtag, width=width, wunit=wunit, initial_weight=initial_weight, temp_weight=temp_weight)
		p.paper_code = paper_code
		p.width = width
		p.wunit = wunit
		p.initial_weight = initial_weight
		p.temp_weight = temp_weight
		p.lane = ilane
		p.position = ipos
		p.save()
#		realtag = ""

		response = "/stock/?pcode="+str(ipcode)+"&width="+str(iwidth)+"&loss="+str(iloss)+"&clamping=no&changed=yes"

	else:
		err = ""
		error = "Your submitted position is not between 1 and 43."
		return render_to_response('submit_error.html', locals())

	return HttpResponseRedirect(response)
