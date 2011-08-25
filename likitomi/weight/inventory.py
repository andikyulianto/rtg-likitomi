# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRolldetails, PaperMovement

def inventory(request):
	if 'pcode' in request.GET and request.GET['pcode']:
		pcode = request.GET['pcode']
	else:
		pcode = ""

	if 'width' in request.GET and request.GET['width']:
		width = request.GET['width']
	else:
		width = ""

	if 'loss' in request.GET and request.GET['loss']:
		loss = request.GET['loss']
		if loss != 'undefined':
			losspx = int(loss)/5.0
			if losspx > 200: losspx = 208 # limited vertical line of required weight
	else:
		loss = ""

	if 'lossarr' in request.GET and request.GET['lossarr']:
		lossarr = request.GET['lossarr']
		if lossarr != 'undefined':
			lossplt = lossarr.split(",")
			losslistpx = list()
			for u in lossplt:
				i = int(u)/5.0
				if i > 200: i = 208 # limited vertical line of required weight
				losslistpx.append(i)
	else:
		lossarr = ""

	if 'spcode' in request.GET and request.GET['spcode']:
		spcode = request.GET['spcode']
	else:
		spcode = ""

	if 'swidth' in request.GET and request.GET['swidth']:
		swidth = request.GET['swidth']
	else:
		swidth = ""

	if 'cpcode' in request.GET and request.GET['cpcode']:
		cpcode = request.GET['cpcode']
	else:
		cpcode = ""

	if 'cwidth' in request.GET and request.GET['cwidth']:
		cwidth = request.GET['cwidth']
	else:
		cwidth = ""

	if 'lane' in request.GET and request.GET['lane']:
		lane = request.GET['lane']
	else:
		lane = ""

	if 'position' in request.GET and request.GET['position']:
		position = request.GET['position']
	else:
		position = ""

	if 'atlane' in request.GET and request.GET['atlane']:
		atlane = request.GET['atlane']
	else:
		atlane = ""

	if 'atposition' in request.GET and request.GET['atposition']:
		atposition = request.GET['atposition']
	else:
		atposition = ""

	if 'clamping' in request.GET and request.GET['clamping']:
		clamping = request.GET['clamping']
	else:
		clamping = "no"

	if 'changed' in request.GET and request.GET['changed']:
		changed = request.GET['changed']
	else:
		changed = "no"

	if 'realtag' in request.GET and request.GET['realtag']:
		realtag = request.GET['realtag']
	else:
		realtag = ""

	if 'loc' in request.GET and request.GET['loc']:
		loc = request.GET['loc']
	else:
		loc = ""

	if 'mappos' in request.GET and request.GET['mappos']:
		mappos = request.GET['mappos']
	else:
		mappos = ""

#	vlane = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

#	laneall = ['H','','G','F','','E','D','','C','B','','A']
#	posall = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#	posh = ['','','3','4','5','6','','8','9','','','','']
#	posg = ['','','3','4','5','6','','8','9','','','','']
#	posf = ['','','3','4','5','6','','8','9','','','','']
#	pose = ['1','2','3','4','5','6','','8','9','','','','']
#	posd = ['1','2','3','4','5','6','','8','9','','','','']
#	posc = ['1','2','3','4','5','6','','8','9','10','11','12','13']
#	posb = ['1','2','3','4','5','6','','8','9','10','11','12','13']
#	posa = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#	buff = ['1','2']

#	pos4 = ['','','3','4','5','6','','8','9','','','','']
#	pos3 = ['1','2','3','4','5','6','','8','9','','','','']
#	pos2 = ['1','2','3','4','5','6','','8','9','10','11','12','13']
#	pos1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

#	posall = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	posall = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
#	pos18_41 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '', '']
	pos18_41 = ['', '', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
#	pos19_40 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']
	pos19_40 = ['', '', '', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']

	vlane = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']

	laneall = ['H','','G','F','','E','D','','C','B','','A']

	posh = ['', '', '', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	posg = ['', '', '', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	posf = ['', '', '', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	pose = ['', '', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	posd = ['', '', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	posc = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
	posb = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
	posa = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']

##	buff = ['1','2']

	pos4 = ['', '', '', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	pos3 = ['', '', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
	pos2 = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']
	pos1 = ['43', '42', '41', '40', '39', '38', '37', '36', '35', '34', '33', '32', '31', '30', '29', '28', '27', '26', '25', '24', '23', '22', '21', '20', '19', '18', '17', '16', '15', '14', '13', '12', '11', '10', '09', '08', '07', '06', '05', '04', '03', '02', '01']

	Alist = list()
	Blist = list()
	Clist = list()

	Dlist = list()
	Elist = list()
	Flist = list()
	Glist = list()
	Hlist = list()

	STlist = list()
	NDlist = list()
	RDlist = list()
	THlist = list()

	zero4 = [0, 0, 0, 0]
	zero8 = [0, 0, 0, 0, 0, 0, 0, 0]
	zero12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	pswitch = "on"
	sswitch = "on"
	cswitch = "on"

###################################################################################################################################################################
# FROM PLAN # ####################################################################################################################################################
###################################################################################################################################################################
	if pcode and width and pswitch == "on":
		query = PaperRolldetails.objects.filter(paper_code=pcode, size=width).values_list('likitomi_roll_id')
		qexists = PaperRolldetails.objects.filter(paper_code=pcode, size=width).exists()

		if qexists == True:
			delist = list()
			wlist = list()
			recwlist = list()
			ridlist = list()
			elist = list()
			wlistpx = list()
			recwlistpx = list()
			dis_wlistpx = list()
			wtop5 = list()
			idtop5 = list()
			pxtop5 = list()

			for item in query:
				totem = list(item)
				delist.append(totem)
				rid = int(totem[0])
				ridlist.append(rid)
				exists = PaperMovement.objects.filter(roll_id=rid).exists()
				elist.append(exists)
				if exists == True:
					weight = int(str(PaperMovement.objects.filter(roll_id=rid).order_by('-created_on').values_list('actual_wt')[0])[1:][:-4])
				else:
					weight = int(str(PaperRolldetails.objects.filter(likitomi_roll_id=rid).values_list('initial_weight')[0])[1:][:-3])
				wlist.append(weight)

			for i,w in enumerate(wlist):
				wpx = int(w)/5.0
				wlistpx.append(wpx)
				if wpx > losspx+50: # How much more than +loss weight? 50?
					recwlistpx.append(wpx)
				if w > int(loss)+50: # How much more than +loss weight? 50?
					recwlist.append(w)
					wtop5.append(wlist[i])
					idtop5.append(str(ridlist[i]))
					pxtop5.append(int(w)/5.0)

			while len(wtop5) > 5:
				i = wtop5.index(max(wtop5))
				wtop5.pop(i)
				idtop5.pop(i)
				pxtop5.pop(i)

			for wpx in pxtop5:
				wpx = wpx-8
				if wpx > 192: wpx = 202.0 # limited symbol out of area
				dis_wlistpx.append(wpx)

			if len(wtop5) > 0: bstchc = min(wtop5)
			else: bstchc = 2000
			if len(pxtop5) > 0:
				bstchcpx = min(pxtop5)
				dis_bstchcpx = bstchcpx-8
			else: bstchcpx = 400

#			recwlistpx.sort()
#			if len(recwlistpx) > 0:
#				bstchcpx = recwlistpx[0]
#				dis_bstchcpx = bstchcpx-8
#			else: bstchcpx = 400
#			recwlist.sort()
#			if len(recwlist) > 0: bstchc = recwlist[0]
#			else: bstchc = 2000

			initial_weight = int(str(PaperRolldetails.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx = initial_weight/5-5

		mquery = PaperRolldetails.objects.filter(paper_code=pcode, size=width).values_list('lane', 'position', 'likitomi_roll_id')
		mexists = PaperRolldetails.objects.filter(paper_code=pcode, size=width).exists()
		mstr = str(mquery)
		mlist = list(mquery)

		top5list = list()
		for i,m in enumerate(mlist):
			if m[2] in idtop5:
				top5list.append(m)

		for ind,pair in enumerate(top5list):
			if pair[0] == 'A':
				posa.pop(43-pair[1])
				posa.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Alist):
					Alist.append([pair[1],0,0,0,0])
				for ls in Alist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'B':
				posb.pop(43-pair[1])
				posb.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Blist):
					Blist.append([pair[1],0,0,0,0])
				for ls in Blist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'C':
				posc.pop(43-pair[1])
				posc.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Clist):
					Clist.append([pair[1],0,0,0,0])
				for ls in Clist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'D':
				posd.pop(43-pair[1])
				posd.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Dlist):
					Dlist.append([pair[1],0,0,0,0])
				for ls in Dlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'E':
				pose.pop(43-pair[1])
				pose.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Elist):
					Elist.append([pair[1],0,0,0,0])
				for ls in Elist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'F':
				posf.pop(43-pair[1])
				posf.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Flist):
					Flist.append([pair[1],0,0,0,0])
				for ls in Flist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'G':
				posg.pop(43-pair[1])
				posg.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Glist):
					Glist.append([pair[1],0,0,0,0])
				for ls in Glist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == 'H':
				posh.pop(43-pair[1])
				posh.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(Hlist):
					Hlist.append([pair[1],0,0,0,0])
				for ls in Hlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == '4':
				pos4.pop(43-pair[1])
				pos4.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(THlist):
					THlist.append([pair[1],0,0,0,0])
				for ls in THlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == '3':
				pos3.pop(43-pair[1])
				pos3.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(RDlist):
					RDlist.append([pair[1],0,0,0,0])
				for ls in RDlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == '2':
				pos2.pop(43-pair[1])
				pos2.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(NDlist):
					NDlist.append([pair[1],0,0,0,0])
				for ls in NDlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

			elif pair[0] == '1':
				pos1.pop(43-pair[1])
				pos1.insert(43-pair[1], str(wlist[ind+1])+"."+str(pair[1]))
				if str(pair[1]) not in str(STlist):
					STlist.append([pair[1],0,0,0,0])
				for ls in STlist:
					if pair[1] == ls[0]:
						if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind+1]:
							ls[1] = ls[1] + 1
						if bstchc and wlist[ind+1] == bstchc:
							if wlist[ind+1] == initial_weight or wlist[ind+1] >= 700:
								ls[4] = ls[4] + .0
							elif 700 > wlist[ind+1] and wlist[ind+1] >= 400:
								ls[3] = ls[3] + .0
							elif 400 > wlist[ind+1] and wlist[ind+1] >= 100:
								ls[2] = ls[2] + .0
							elif 100 > wlist[ind+1]:
								ls[1] = ls[1] + .0

###################################################################################################################################################################
# FROM SEARCH # ##################################################################################################################################################
###################################################################################################################################################################
	if spcode != "undefined" and swidth != "undefined" and spcode != "" and swidth != "" and sswitch == "on":
		query2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).values_list('likitomi_roll_id')
		qexists2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).exists()

		if qexists2 == True:
			delist2 = list()
			wlist2 = list()
			ridlist2 = list()
			elist2 = list()
			wlistpx2 = list()
			dis_wlistpx2 = list()

			for item in query2:
				totem = list(item)
				delist2.append(totem)
				rid = int(totem[0])
				ridlist2.append(rid)
				exists = PaperMovement.objects.filter(roll_id=rid).exists()
				elist2.append(exists)
				if exists == True:
					weight = int(str(PaperMovement.objects.filter(roll_id=rid).order_by('-created_on').values_list('actual_wt')[0])[1:][:-4])
				else:
					weight = int(str(PaperRolldetails.objects.filter(likitomi_roll_id=rid).values_list('initial_weight')[0])[1:][:-3])
				wlist2.append(weight)

			for w in wlist2:
				wpx = int(w)/5.0
				wlistpx2.append(wpx)

			for wpx in wlistpx2:
				wpx = wpx-8
				if wpx > 192: wpx = 202.0 # limited symbol out of area
				dis_wlistpx2.append(wpx)

			initial_weight2 = int(str(PaperRolldetails.objects.filter(paper_code=spcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx2 = initial_weight2/5-5

		mquery2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).values_list('lane', 'position')
		mexists2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).exists()
		mstr2 = str(mquery2)
		mlist2 = list(mquery2)

		for ind,pair in enumerate(mlist2):
			if pair[0] == 'A':
				posa.pop(43-pair[1])
				posa.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Alist):
					Alist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Alist:
						if ls[0] == pair[1]:
							try:
								dexa = Alist.index(ls)
								Alist[dexa].extend(zero4)
							except: pass
				for ls in Alist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'B':
				posb.pop(43-pair[1])
				posb.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Blist):
					Blist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Blist:
						if ls[0] == pair[1]:
							try:
								dexb = Blist.index(ls)
								Blist[dexb].extend(zero4)
							except: pass
				for ls in Blist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'C':
				posc.pop(43-pair[1])
				posc.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Clist):
					Clist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Clist:
						if ls[0] == pair[1]:
							try:
								dexc = Clist.index(ls)
								Clist[dexc].extend(zero4)
							except: pass
				for ls in Clist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'D':
				posd.pop(43-pair[1])
				posd.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Dlist):
					Dlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Dlist:
						if ls[0] == pair[1]:
							try:
								dexd = Dlist.index(ls)
								Dlist[dexd].extend(zero4)
							except: pass
				for ls in Dlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'E':
				pose.pop(43-pair[1])
				pose.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Elist):
					Elist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Elist:
						if ls[0] == pair[1]:
							try:
								dexe = Elist.index(ls)
								Elist[dexe].extend(zero4)
							except: pass
				for ls in Elist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'F':
				posf.pop(43-pair[1])
				posf.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Flist):
					Flist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Flist:
						if ls[0] == pair[1]:
							try:
								dexf = Flist.index(ls)
								Flist[dexf].extend(zero4)
							except: pass
				for ls in Flist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'G':
				posg.pop(43-pair[1])
				posg.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Glist):
					Glist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Glist:
						if ls[0] == pair[1]:
							try:
								dexg = Glist.index(ls)
								Glist[dexg].extend(zero4)
							except: pass
				for ls in Glist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == 'H':
				posh.pop(43-pair[1])
				posh.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Hlist):
					Hlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in Hlist:
						if ls[0] == pair[1]:
							try:
								dexh = Hlist.index(ls)
								Hlist[dexh].extend(zero4)
							except: pass
				for ls in Hlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == '4':
				pos4.pop(43-pair[1])
				pos4.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(THlist):
					THlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in THlist:
						if ls[0] == pair[1]:
							try:
								dex4 = THlist.index(ls)
								THlist[dex4].extend(zero4)
							except: pass
				for ls in THlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == '3':
				pos3.pop(43-pair[1])
				pos3.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(RDlist):
					RDlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in RDlist:
						if ls[0] == pair[1]:
							try:
								dex3 = RDlist.index(ls)
								RDlist[dex3].extend(zero4)
							except: pass
				for ls in RDlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == '2':
				pos2.pop(43-pair[1])
				pos2.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(NDlist):
					NDlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in NDlist:
						if ls[0] == pair[1]:
							try:
								dex2 = NDlist.index(ls)
								NDlist[dex2].extend(zero4)
							except: pass
				for ls in NDlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

			elif pair[0] == '1':
				pos1.pop(43-pair[1])
				pos1.insert(43-pair[1], str(wlist2[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(STlist):
					STlist.append([pair[1],0,0,0,0,0,0,0,0])
				else:
					for ls in STlist:
						if ls[0] == pair[1]:
							try:
								dex1 = STlist.index(ls)
								STlist[dex1].extend(zero4)
							except: pass
				for ls in STlist:
					if pair[1] == ls[0]:
						if wlist2[ind] == initial_weight2 or wlist2[ind] >= 700:
							ls[8] = ls[8] + 1
						elif 700 > wlist2[ind] and wlist2[ind] >= 400:
							ls[7] = ls[7] + 1
						elif 400 > wlist2[ind] and wlist2[ind] >= 100:
							ls[6] = ls[6] + 1
						elif 100 > wlist2[ind]:
							ls[5] = ls[5] + 1

###################################################################################################################################################################
# FROM CLAMPLIFT # ###############################################################################################################################################
###################################################################################################################################################################
	if cpcode != "" and cwidth != "" and cpcode != "undefined" and cwidth != "undefined" and cswitch == "on":
		query3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).values_list('likitomi_roll_id')
		qexists3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).exists()

		if qexists3 == True:
			delist3 = list()
			wlist3 = list()
			ridlist3 = list()
			elist3 = list()
			wlistpx3 = list()
			dis_wlistpx3 = list()

			for item in query3:
				totem = list(item)
				delist3.append(totem)
				rid = int(totem[0])
				ridlist3.append(rid)
				exists = PaperMovement.objects.filter(roll_id=rid).exists()
				elist3.append(exists)
				if exists == True:
					weight = int(str(PaperMovement.objects.filter(roll_id=rid).order_by('-created_on').values_list('actual_wt')[0])[1:][:-4])
				else:
					weight = int(str(PaperRolldetails.objects.filter(likitomi_roll_id=rid).values_list('initial_weight')[0])[1:][:-3])
				wlist3.append(weight)

			for w in wlist3:
				wpx = int(w)/5.0
				wlistpx3.append(wpx)

			for wpx in wlistpx3:
				wpx = wpx-8
				if wpx > 192: wpx = 202.0 # limited symbol out of area
				dis_wlistpx3.append(wpx)

			initial_weight3 = int(str(PaperRolldetails.objects.filter(paper_code=cpcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx3 = initial_weight3/5-5

		mquery3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).values_list('lane', 'position')
		mexists3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).exists()
		mstr3 = str(mquery3)
		mlist3 = list(mquery3)

		for ind,pair in enumerate(mlist3):
			if pair[0] == 'A':
				posa.pop(43-pair[1])
				posa.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Alist):
					Alist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Alist:
						if ls[0] == pair[1]:
							try:
								dexa = Alist.index(ls)
								if len(Alist[dexa]) == 5: Alist[dexa].extend(zero8)
								if len(Alist[dexa]) == 9: Alist[dexa].extend(zero4)
							except: pass
				for ls in Alist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'B':
				posb.pop(43-pair[1])
				posb.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Blist):
					Blist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Blist:
						if ls[0] == pair[1]:
							try:
								dexb = Blist.index(ls)
								if len(Blist[dexb]) == 5: Blist[dexb].extend(zero8)
								if len(Blist[dexb]) == 9: Blist[dexb].extend(zero4)
							except: pass
				for ls in Blist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'C':
				posc.pop(43-pair[1])
				posc.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Clist):
					Clist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Clist:
						if ls[0] == pair[1]:
							try:
								dexc = Clist.index(ls)
								if len(Clist[dexc]) == 5: Clist[dexc].extend(zero8)
								if len(Clist[dexc]) == 9: Clist[dexc].extend(zero4)
							except: pass
				for ls in Clist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'D':
				posd.pop(43-pair[1])
				posd.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Dlist):
					Dlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Dlist:
						if ls[0] == pair[1]:
							try:
								dexd = Dlist.index(ls)
								if len(Dlist[dexd]) == 5: Dlist[dexd].extend(zero8)
								if len(Dlist[dexd]) == 9: Dlist[dexd].extend(zero4)
							except: pass
				for ls in Dlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'E':
				pose.pop(43-pair[1])
				pose.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Elist):
					Elist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Elist:
						if ls[0] == pair[1]:
							try:
								dexe = Elist.index(ls)
								if len(Elist[dexe]) == 5: Elist[dexe].extend(zero8)
								if len(Elist[dexe]) == 9: Elist[dexe].extend(zero4)
							except: pass

				for ls in Elist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'F':
				posf.pop(43-pair[1])
				posf.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Flist):
					Flist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Flist:
						if ls[0] == pair[1]:
							try:
								dexf = Flist.index(ls)
								if len(Flist[dexf]) == 5: Flist[dexf].extend(zero8)
								if len(Flist[dexf]) == 9: Flist[dexf].extend(zero4)
							except: pass
				for ls in Flist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'G':
				posg.pop(43-pair[1])
				posg.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Glist):
					Glist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Glist:
						if ls[0] == pair[1]:
							try:
								dexg = Glist.index(ls)
								if len(Glist[dexg]) == 5: Glist[dexg].extend(zero8)
								if len(Glist[dexg]) == 9: Glist[dexg].extend(zero4)
							except: pass
				for ls in Glist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == 'H':
				posh.pop(43-pair[1])
				posh.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(Hlist):
					Hlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in Hlist:
						if ls[0] == pair[1]:
							try:
								dexh = Hlist.index(ls)
								if len(Hlist[dexh]) == 5: Hlist[dexh].extend(zero8)
								if len(Hlist[dexh]) == 9: Hlist[dexh].extend(zero4)
							except: pass
				for ls in Hlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == '4':
				pos4.pop(43-pair[1])
				pos4.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(THlist):
					THlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in THlist:
						if ls[0] == pair[1]:
							try:
								dex4 = THlist.index(ls)
								if len(THlist[dex4]) == 5: THlist[dex4].extend(zero8)
								if len(THlist[dex4]) == 9: THlist[dex4].extend(zero4)
							except: pass
				for ls in THlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == '3':
				pos3.pop(43-pair[1])
				pos3.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(RDlist):
					RDlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in RDlist:
						if ls[0] == pair[1]:
							try:
								dex3 = RDlist.index(ls)
								if len(RDlist[dex3]) == 5: RDlist[dex3].extend(zero8)
								if len(RDlist[dex3]) == 9: RDlist[dex3].extend(zero4)
							except: pass
				for ls in RDlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == '2':
				pos2.pop(43-pair[1])
				pos2.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(NDlist):
					NDlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in NDlist:
						if ls[0] == pair[1]:
							try:
								dex2 = NDlist.index(ls)
								if len(NDlist[dex2]) == 5: NDlist[dex2].extend(zero8)
								if len(NDlist[dex2]) == 9: NDlist[dex2].extend(zero4)
							except: pass
				for ls in NDlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

			elif pair[0] == '1':
				pos1.pop(43-pair[1])
				pos1.insert(43-pair[1], str(wlist3[ind])+"."+str(pair[1]))
				if str(pair[1]) not in str(STlist):
					STlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
				else:
					for ls in STlist:
						if ls[0] == pair[1]:
							try:
								dex1 = STlist.index(ls)
								if len(STlist[dex1]) == 5: STlist[dex1].extend(zero8)
								if len(STlist[dex1]) == 9: STlist[dex1].extend(zero4)
							except: pass
				for ls in STlist:
					if pair[1] == ls[0]:
						if wlist3[ind] == initial_weight3 or wlist3[ind] >= 700:
							ls[12] = ls[12] + 1
						elif 700 > wlist3[ind] and wlist3[ind] >= 400:
							ls[11] = ls[11] + 1
						elif 400 > wlist3[ind] and wlist3[ind] >= 100:
							ls[10] = ls[10] + 1
						elif 100 > wlist3[ind]:
							ls[9] = ls[9] + 1

# FLOATING VEHICLE #
	if len(str(atposition)) == 1: catposition = "0"+atposition
	else: catposition = atposition
	for ind,item in enumerate(pos1):
		if item == catposition and atlane == '1':
			pos1.pop(ind)
			pos1.insert(ind,"*")
		if item.find(".") != -1 and str(43-ind) == str(atposition):
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = isplt[0]+"."+isplt[1]
			pos1.pop(ind)
			pos1.insert(ind,vios)

	for ind,item in enumerate(pos2):
		if item == catposition and atlane == '2':
			pos2.pop(ind)
			pos2.insert(ind,"*")
		if item.find(".") != -1 and str(43-ind) == str(atposition):
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = isplt[0]+"."+isplt[1]
			pos2.pop(ind)
			pos2.insert(ind,vios)

	for ind,item in enumerate(pos3):
		if item == catposition and atlane == '3':
			pos3.pop(ind)
			pos3.insert(ind,"*")
		if item.find(".") != -1 and str(43-ind) == str(atposition):
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = isplt[0]+"."+isplt[1]
			pos3.pop(ind)
			pos3.insert(ind,vios)

	for ind,item in enumerate(pos4):
		if item == catposition and atlane == '4':
			pos4.pop(ind)
			pos4.insert(ind,"*")
		if item.find(".") != -1 and str(43-ind) == str(atposition):
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = isplt[0]+"."+isplt[1]
			pos4.pop(ind)
			pos4.insert(ind,vios)

	if atlane == '1':
		leftlane = 'B'
		rightlane = 'A'
	if atlane == '2':
		leftlane = 'D'
		rightlane = 'C'
	if atlane == '3':
		leftlane = 'F'
		rightlane = 'E'
	if atlane == '4':
		leftlane = 'H'
		rightlane = 'G'

# MANUAL CHANGE LOCATION #
	if loc == "up" or loc == "down":
		if loc == 'up': plane = leftlane
		if loc == 'down': plane = rightlane
		PaperRolldetails.objects.filter(likitomi_roll_id=realtag).update(lane=plane, position=atposition)

# AUTO CHANGE LOCATION #
	if clamping == "yes" and changed == "no":
		PaperRolldetails.objects.filter(likitomi_roll_id=realtag).update(lane=atlane,position=atposition)

	return render_to_response('inventory.html', locals())
