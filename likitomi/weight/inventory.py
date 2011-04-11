# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRoll, PaperHistory

def inventory(request):
	try:
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
			losspx = int(loss)/5 - 5
			if losspx > 194:
				losspx = 200
			lossinv = 200-losspx
		else:
			loss = ""

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

		vlane = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

		laneall = ['H','','G','F','','E','D','','C','B','','A']
		posall = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
		posh = ['','','3','4','5','6','','8','9','','','','']
		posg = ['','','3','4','5','6','','8','9','','','','']
		posf = ['','','3','4','5','6','','8','9','','','','']
		pose = ['1','2','3','4','5','6','','8','9','','','','']
		posd = ['1','2','3','4','5','6','','8','9','','','','']
		posc = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		posb = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		posa = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
		buff = ['1','2']

		pos4 = ['','','3','4','5','6','','8','9','','','','']
		pos3 = ['1','2','3','4','5','6','','8','9','','','','']
		pos2 = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		pos1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

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
			query = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('id')
			qexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()

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
					exists = PaperHistory.objects.filter(roll_id=rid).exists()
					elist.append(exists)
					if exists == True:
						weight = int(str(PaperHistory.objects.filter(roll_id=rid).order_by('-timestamp').values_list('last_wt')[0])[1:][:-3])
					else:
						weight = int(str(PaperRoll.objects.filter(id=rid).values_list('initial_weight')[0])[1:][:-3])
					wlist.append(weight)

				for w in wlist:
					wpx = int(w)/5 - 5
					if wpx > 194:
						wpx = 200
					wlistpx.append(wpx)

				initial_weight = int(str(PaperRoll.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])
				initialpx = initial_weight/5 - 5

			mquery = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('lane', 'position')
			mexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()
			mstr = str(mquery)
			mlist = list(mquery)

			for ind,pair in enumerate(mlist):
				if pair[0] == u'A':
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

				elif pair[0] == u'B':
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

				elif pair[0] == u'C':
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

				elif pair[0] == u'D':
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

				elif pair[0] == u'E':
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

				elif pair[0] == u'F':
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

				elif pair[0] == u'G':
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

				elif pair[0] == u'H':
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

				elif pair[0] == u'4':
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

				elif pair[0] == u'3':
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

				elif pair[0] == u'2':
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

				elif pair[0] == u'1':
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
		if spcode and swidth and sswitch == "on":
			query2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).values_list('id')
			qexists2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).exists()

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
					exists = PaperHistory.objects.filter(roll_id=rid).exists()
					elist2.append(exists)
					if exists == True:
						weight = int(str(PaperHistory.objects.filter(roll_id=rid).order_by('-timestamp').values_list('last_wt')[0])[1:][:-3])
					else:
						weight = int(str(PaperRoll.objects.filter(id=rid).values_list('initial_weight')[0])[1:][:-3])
					wlist2.append(weight)

				for w in wlist2:
					wpx = int(w)/5 - 5
					if wpx > 194:
						wpx = 200
					wlistpx2.append(wpx)

				initial_weight2 = int(str(PaperRoll.objects.filter(paper_code=spcode).values_list('initial_weight')[0])[1:][:-3])
				initialpx2 = initial_weight2/5 - 5

			mquery2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).values_list('lane', 'position')
			mexists2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).exists()
			mstr2 = str(mquery2)
			mlist2 = list(mquery2)

			for ind,pair in enumerate(mlist2):
				if pair[0] == u'A':
					posa.pop(pair[1]-1)
					posa.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Alist):
						Alist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Alist:
							if ls[0] == pair[1]:
								dex = Alist.index(ls)
						Alist[dex].extend(zero4)
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

				elif pair[0] == u'B':
					posb.pop(pair[1]-1)
					posb.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Blist):
						Blist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Blist:
							if ls[0] == pair[1]:
								dex = Blist.index(ls)
						Blist[dex].extend(zero4)
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

				elif pair[0] == u'C':
					posc.pop(pair[1]-1)
					posc.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Clist):
						Clist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Clist:
							if ls[0] == pair[1]:
								dex = Clist.index(ls)
						Clist[dex].extend(zero4)
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

				elif pair[0] == u'D':
					posd.pop(pair[1]-1)
					posd.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Dlist):
						Dlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Dlist:
							if ls[0] == pair[1]:
								dex = Dlist.index(ls)
						Dlist[dex].extend(zero4)
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

				elif pair[0] == u'E':
					pose.pop(pair[1]-1)
					pose.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Elist):
						Elist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Elist:
							if ls[0] == pair[1]:
								dex = Elist.index(ls)
						Elist[dex].extend(zero4)
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

				elif pair[0] == u'F':
					posf.pop(pair[1]-1)
					posf.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Flist):
						Flist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Flist:
							if ls[0] == pair[1]:
								dex = Flist.index(ls)
						Flist[dex].extend(zero4)
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

				elif pair[0] == u'G':
					posg.pop(pair[1]-1)
					posg.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Glist):
						Glist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Glist:
							if ls[0] == pair[1]:
								dex = Glist.index(ls)
						Glist[dex].extend(zero4)
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

				elif pair[0] == u'H':
					posh.pop(pair[1]-1)
					posh.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Hlist):
						Hlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in Hlist:
							if ls[0] == pair[1]:
								dex = Hlist.index(ls)
						Hlist[dex].extend(zero4)
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

				elif pair[0] == u'4':
					pos4.pop(pair[1]-1)
					pos4.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(THlist):
						THlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in THlist:
							if ls[0] == pair[1]:
								dex = THlist.index(ls)
						THlist[dex].extend(zero4)
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

				elif pair[0] == u'3':
					pos3.pop(pair[1]-1)
					pos3.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(RDlist):
						RDlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in RDlist:
							if ls[0] == pair[1]:
								dex = RDlist.index(ls)
						RDlist[dex].extend(zero4)
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

				elif pair[0] == u'2':
					pos2.pop(pair[1]-1)
					pos2.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(NDlist):
						NDlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in NDlist:
							if ls[0] == pair[1]:
								dex = NDlist.index(ls)
						NDlist[dex].extend(zero4)
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

				elif pair[0] == u'1':
					pos1.pop(pair[1]-1)
					pos1.insert(pair[1]-1, float(str(wlist2[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(STlist):
						STlist.append([pair[1],0,0,0,0,0,0,0,0])
					else:
						for ls in STlist:
							if ls[0] == pair[1]:
								dex = STlist.index(ls)
						STlist[dex].extend(zero4)
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
		if cpcode and cwidth and cswitch == "on":
			query3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).values_list('id')
			qexists3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).exists()

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
					exists = PaperHistory.objects.filter(roll_id=rid).exists()
					elist3.append(exists)
					if exists == True:
						weight = int(str(PaperHistory.objects.filter(roll_id=rid).order_by('-timestamp').values_list('last_wt')[0])[1:][:-3])
					else:
						weight = int(str(PaperRoll.objects.filter(id=rid).values_list('initial_weight')[0])[1:][:-3])
					wlist3.append(weight)

				for w in wlist3:
					wpx = int(w)/5 - 5
					if wpx > 194:
						wpx = 200
					wlistpx3.append(wpx)

				initial_weight3 = int(str(PaperRoll.objects.filter(paper_code=cpcode).values_list('initial_weight')[0])[1:][:-3])
				initialpx3 = initial_weight3/5 - 5

			mquery3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).values_list('lane', 'position')
			mexists3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).exists()
			mstr3 = str(mquery3)
			mlist3 = list(mquery3)

			for ind,pair in enumerate(mlist3):
				if pair[0] == u'A':
					posa.pop(pair[1]-1)
					posa.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Alist):
						Alist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Alist:
							if ls[0] == pair[1]:
								dex = Alist.index(ls)
						if len(Alist[dex]) == 5: Alist[dex].extend(zero8)
						if len(Alist[dex]) == 9: Alist[dex].extend(zero4)
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

				elif pair[0] == u'B':
					posb.pop(pair[1]-1)
					posb.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Blist):
						Blist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Blist:
							if ls[0] == pair[1]:
								dex = Blist.index(ls)
						if len(Blist[dex]) == 5: Blist[dex].extend(zero8)
						if len(Blist[dex]) == 9: Blist[dex].extend(zero4)
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

				elif pair[0] == u'C':
					posc.pop(pair[1]-1)
					posc.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Clist):
						Clist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Clist:
							if ls[0] == pair[1]:
								dex = Clist.index(ls)
						if len(Clist[dex]) == 5: Clist[dex].extend(zero8)
						if len(Clist[dex]) == 9: Clist[dex].extend(zero4)
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

				elif pair[0] == u'D':
					posd.pop(pair[1]-1)
					posd.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Dlist):
						Dlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Dlist:
							if ls[0] == pair[1]:
								dex = Dlist.index(ls)
						if len(Dlist[dex]) == 5: Dlist[dex].extend(zero8)
						if len(Dlist[dex]) == 9: Dlist[dex].extend(zero4)
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

				elif pair[0] == u'E':
					pose.pop(pair[1]-1)
					pose.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Elist):
						Elist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Elist:
							if ls[0] == pair[1]:
								dex = Elist.index(ls)
						if len(Elist[dex]) == 5: Elist[dex].extend(zero8)
						if len(Elist[dex]) == 9: Elist[dex].extend(zero4)
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

				elif pair[0] == u'F':
					posf.pop(pair[1]-1)
					posf.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Flist):
						Flist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Flist:
							if ls[0] == pair[1]:
								dex = Flist.index(ls)
						if len(Flist[dex]) == 5: Flist[dex].extend(zero8)
						if len(Flist[dex]) == 9: Flist[dex].extend(zero4)
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

				elif pair[0] == u'G':
					posg.pop(pair[1]-1)
					posg.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Glist):
						Glist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Glist:
							if ls[0] == pair[1]:
								dex = Glist.index(ls)
						if len(Glist[dex]) == 5: Glist[dex].extend(zero8)
						if len(Glist[dex]) == 9: Glist[dex].extend(zero4)
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

				elif pair[0] == u'H':
					posh.pop(pair[1]-1)
					posh.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(Hlist):
						Hlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in Hlist:
							if ls[0] == pair[1]:
								dex = Hlist.index(ls)
						if len(Hlist[dex]) == 5: Hlist[dex].extend(zero8)
						if len(Hlist[dex]) == 9: Hlist[dex].extend(zero4)
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

				elif pair[0] == u'4':
					pos4.pop(pair[1]-1)
					pos4.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(THlist):
						THlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in THlist:
							if ls[0] == pair[1]:
								dex = THlist.index(ls)
						if len(THlist[dex]) == 5: THlist[dex].extend(zero8)
						if len(THlist[dex]) == 9: THlist[dex].extend(zero4)
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

				elif pair[0] == u'3':
					pos3.pop(pair[1]-1)
					pos3.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(RDlist):
						RDlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in RDlist:
							if ls[0] == pair[1]:
								dex = RDlist.index(ls)
						if len(RDlist[dex]) == 5: RDlist[dex].extend(zero8)
						if len(RDlist[dex]) == 9: RDlist[dex].extend(zero4)
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

				elif pair[0] == u'2':
					pos2.pop(pair[1]-1)
					pos2.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(NDlist):
						NDlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in NDlist:
							if ls[0] == pair[1]:
								dex = NDlist.index(ls)
						if len(NDlist[dex]) == 5: NDlist[dex].extend(zero8)
						if len(NDlist[dex]) == 9: NDlist[dex].extend(zero4)
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

				elif pair[0] == u'1':
					pos1.pop(pair[1]-1)
					pos1.insert(pair[1]-1, float(str(wlist3[ind])+"."+str(pair[1])))
					if str(pair[1]) not in str(STlist):
						STlist.append([pair[1],0,0,0,0,0,0,0,0,0,0,0,0])
					else:
						for ls in STlist:
							if ls[0] == pair[1]:
								dex = STlist.index(ls)
						if len(STlist[dex]) == 5: STlist[dex].extend(zero8)
						if len(STlist[dex]) == 9: STlist[dex].extend(zero4)
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

#		STlist = [[4L,1,1,1,1,1,1,1,1,1,1,1,1]]

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
			if loc == 'up': p.lane = leftlane
			if loc == 'down': p.lane = rightlane
			p.position = atposition
			p.save()

# AUTO CHANGE LOCATION #
		if clamping == "yes" and changed == "no":
			ccquery = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'temp_weight')[0]
			ccqlist = list(ccquery)
			paper_code = ccqlist[0]
			width = ccqlist[1]
			wunit = ccqlist[2]
			initial_weight = ccqlist[3]
			temp_weight = ccqlist[4]
			p = PaperRoll(id=realtag, width=width, wunit=wunit, initial_weight=initial_weight, temp_weight=temp_weight)
			p.paper_code = paper_code
			p.width = width
			p.wunit = wunit
			p.initial_weight = initial_weight
			p.temp_weight = temp_weight
			p.lane = atlane
			p.position = atposition
			p.save()

	except:
		pass

	return render_to_response('inventory.html', locals())
