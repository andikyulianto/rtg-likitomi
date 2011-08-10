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
			losspx = int(loss)/5
			if losspx > 199:
				losspx = 205
			lossinv = 205-losspx
	else:
		loss = ""

	if 'lossarr' in request.GET and request.GET['lossarr']:
		lossarr = request.GET['lossarr']
		if lossarr != 'undefined':
			lossplt = lossarr.split(",")
			losslist = list()
			for u in lossplt:
				i = int(u)/5
				if i > 199: i = 205
				losslist.append(i)
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

	posall = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	pos18_41 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '', '']
	pos19_40 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']

	vlane = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']

	laneall = ['H','','G','F','','E','D','','C','B','','A']

	posh = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']
	posg = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']
	posf = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']
	pose = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '', '']
	posd = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '', '']
	posc = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	posb = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	posa = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	buff = ['1','2']

	pos4 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '', '', '']
	pos3 = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '', '']
	pos2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']
	pos1 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43']

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
			ridlist = list()
			elist = list()
			wlistpx = list()

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

			for w in wlist:
				wpx = int(w)/5 - 5
				if wpx > 194:
					wpx = 200
				wlistpx.append(wpx)

			initial_weight = int(str(PaperRolldetails.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx = initial_weight/5 - 5

		mquery = PaperRolldetails.objects.filter(paper_code=pcode, size=width).values_list('lane', 'position')
		mexists = PaperRolldetails.objects.filter(paper_code=pcode, size=width).exists()
		mstr = str(mquery)
		mlist = list(mquery)

		for ind,pair in enumerate(mlist):
			if pair[0] == 'A':
				posa.pop(pair[1]-1)
				posa.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Alist):
					Alist.append([pair[1],0,0,0,0])
				for ls in Alist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'B':
				posb.pop(pair[1]-1)
				posb.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Blist):
					Blist.append([pair[1],0,0,0,0])
				for ls in Blist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'C':
				posc.pop(pair[1]-1)
				posc.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Clist):
					Clist.append([pair[1],0,0,0,0])
				for ls in Clist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'D':
				posd.pop(pair[1]-1)
				posd.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Dlist):
					Dlist.append([pair[1],0,0,0,0])
				for ls in Dlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'E':
				pose.pop(pair[1]-1)
				pose.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Elist):
					Elist.append([pair[1],0,0,0,0])
				for ls in Elist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'F':
				posf.pop(pair[1]-1)
				posf.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Flist):
					Flist.append([pair[1],0,0,0,0])
				for ls in Flist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'G':
				posg.pop(pair[1]-1)
				posg.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Glist):
					Glist.append([pair[1],0,0,0,0])
				for ls in Glist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == 'H':
				posh.pop(pair[1]-1)
				posh.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(Hlist):
					Hlist.append([pair[1],0,0,0,0])
				for ls in Hlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == '4':
				pos4.pop(pair[1]-1)
				pos4.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(THlist):
					THlist.append([pair[1],0,0,0,0])
				for ls in THlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == '3':
				pos3.pop(pair[1]-1)
				pos3.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(RDlist):
					RDlist.append([pair[1],0,0,0,0])
				for ls in RDlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == '2':
				pos2.pop(pair[1]-1)
				pos2.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(NDlist):
					NDlist.append([pair[1],0,0,0,0])
				for ls in NDlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

			elif pair[0] == '1':
				pos1.pop(pair[1]-1)
				pos1.insert(pair[1]-1, float(str(wlist[ind])+"."+str(pair[1])))
				if str(pair[1]) not in str(STlist):
					STlist.append([pair[1],0,0,0,0])
				for ls in STlist:
					if pair[1] == ls[0]:
						if wlist[ind] == initial_weight or wlist[ind] >= 700:
							ls[4] = ls[4] + 1
						elif 700 > wlist[ind] and wlist[ind] >= 400:
							ls[3] = ls[3] + 1
						elif 400 > wlist[ind] and wlist[ind] >= 100:
							ls[2] = ls[2] + 1
						elif 100 > wlist[ind]:
							ls[1] = ls[1] + 1

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
				wpx = int(w)/5 - 5
				if wpx > 194:
					wpx = 200
				wlistpx2.append(wpx)

			initial_weight2 = int(str(PaperRolldetails.objects.filter(paper_code=spcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx2 = initial_weight2/5 - 5

		mquery2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).values_list('lane', 'position')
		mexists2 = PaperRolldetails.objects.filter(paper_code=spcode, size=swidth).exists()
		mstr2 = str(mquery2)
		mlist2 = list(mquery2)

		for ind,pair in enumerate(mlist2):
			if pair[0] == 'A':
				posa.pop(pair[1]-1)
				posa.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posb.pop(pair[1]-1)
				posb.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posc.pop(pair[1]-1)
				posc.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posd.pop(pair[1]-1)
				posd.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				pose.pop(pair[1]-1)
				pose.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posf.pop(pair[1]-1)
				posf.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posg.pop(pair[1]-1)
				posg.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				posh.pop(pair[1]-1)
				posh.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				pos4.pop(pair[1]-1)
				pos4.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				pos3.pop(pair[1]-1)
				pos3.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				pos2.pop(pair[1]-1)
				pos2.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				pos1.pop(pair[1]-1)
				pos1.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
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
				wpx = int(w)/5 - 5
				if wpx > 194:
					wpx = 200
				wlistpx3.append(wpx)

			initial_weight3 = int(str(PaperRolldetails.objects.filter(paper_code=cpcode).values_list('initial_weight')[0])[1:][:-3])
			initialpx3 = initial_weight3/5 - 5

		mquery3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).values_list('lane', 'position')
		mexists3 = PaperRolldetails.objects.filter(paper_code=cpcode, size=cwidth).exists()
		mstr3 = str(mquery3)
		mlist3 = list(mquery3)

		for ind,pair in enumerate(mlist3):
			if pair[0] == 'A':
				posa.pop(pair[1]-1)
				posa.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posb.pop(pair[1]-1)
				posb.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posc.pop(pair[1]-1)
				posc.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posd.pop(pair[1]-1)
				posd.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				pose.pop(pair[1]-1)
				pose.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posf.pop(pair[1]-1)
				posf.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posg.pop(pair[1]-1)
				posg.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				posh.pop(pair[1]-1)
				posh.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				pos4.pop(pair[1]-1)
				pos4.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				pos3.pop(pair[1]-1)
				pos3.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				pos2.pop(pair[1]-1)
				pos2.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
				pos1.pop(pair[1]-1)
				pos1.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
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
	for ind,item in enumerate(pos1):
		if item == atposition and atlane == '1':
			pos1.pop(ind)
			pos1.insert(ind,"*")
		if str(type(item)) == str(type(1.68)) and str(ind+1) == atposition:
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = float(isplt[0]+"."+isplt[1])
			pos1.pop(ind)
			pos1.insert(ind,vios)

	for ind,item in enumerate(pos2):
		if item == atposition and atlane == '2':
			pos2.pop(ind)
			pos2.insert(ind,"*")
		if str(type(item)) == str(type(1.68)) and str(ind+1) == atposition:
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = float(isplt[0]+"."+isplt[1])
			pos2.pop(ind)
			pos2.insert(ind,vios)

	for ind,item in enumerate(pos3):
		if item == atposition and atlane == '3':
			pos3.pop(ind)
			pos3.insert(ind,"*")
		if str(type(item)) == str(type(1.68)) and str(ind+1) == atposition:
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = float(isplt[0]+"."+isplt[1])
			pos3.pop(ind)
			pos3.insert(ind,vios)

	for ind,item in enumerate(pos4):
		if item == atposition and atlane == '4':
			pos4.pop(ind)
			pos4.insert(ind,"*")
		if str(type(item)) == str(type(1.68)) and str(ind+1) == atposition:
			istr = str(item)
			isplt = istr.split(".")
			isplt[0] = "-"+isplt[0]
			vios = float(isplt[0]+"."+isplt[1])
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
