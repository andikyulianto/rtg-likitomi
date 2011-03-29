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
			losspx = int(loss)/4
			if losspx > 250:
				losspx = 250
			lossinv = 250-losspx
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
			clamping = "inv"

		if 'changed' in request.GET and request.GET['changed']:
			changed = request.GET['changed']
		else:
			changed = "inv"



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



# FROM SEARCH #
		if spcode != "" and swidth != "":
			query2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).values_list('id')
			qexists2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).exists()

			if qexists2 == True:
				delist2 = list()
				wlist2 = list()
				ridlist2 = list()
				elist2 = list()

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
					for totem in delist2:
						totem.append(weight)

				initial_weight2 = int(str(PaperRoll.objects.filter(paper_code=spcode).values_list('initial_weight')[0])[1:][:-3])

			mquery2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).values_list('lane', 'position')
			mexists2 = PaperRoll.objects.filter(paper_code=spcode, width=swidth).exists()
			mstr2 = str(mquery2)
			mlist2 = list(mquery2)

			for ind,pair in enumerate(mlist2):
				if pair[0] == u'A':
					ind1 = mlist2.index(pair)
					posa.pop(pair[1]-1)
					posa.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Alist):
						Alist.append([pair[1]])
						Alist[-1].extend(zero4)
					Alist[-1].extend(zero8)
					for ls in Alist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'B':
					ind1 = mlist2.index(pair)
					posb.pop(pair[1]-1)
					posb.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Blist):
						Blist.append([pair[1]])
						Blist[-1].extend(zero4)
					Blist[-1].extend(zero8)
					for ls in Blist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'C':
					ind1 = mlist2.index(pair)
					posc.pop(pair[1]-1)
					posc.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Clist):
						Clist.append([pair[1]])
						Clist[-1].extend(zero4)
					Clist[-1].extend(zero8)
					for ls in Clist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'D':
					ind1 = mlist2.index(pair)
					posd.pop(pair[1]-1)
					posd.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Dlist):
						Dlist.append([pair[1]])
						Dlist[-1].extend(zero4)
					Dlist[-1].extend(zero8)
					for ls in Dlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'E':
					ind1 = mlist2.index(pair)
					pose.pop(pair[1]-1)
					pose.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Elist):
						Elist.append([pair[1]])
						Elist[-1].extend(zero4)
					Elist[-1].extend(zero8)
					for ls in Elist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'F':
					ind1 = mlist2.index(pair)
					posf.pop(pair[1]-1)
					posf.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Flist):
						Flist.append([pair[1]])
						Flist[-1].extend(zero4)
					Flist[-1].extend(zero8)
					for ls in Flist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'G':
					ind1 = mlist2.index(pair)
					posg.pop(pair[1]-1)
					posg.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Glist):
						Glist.append([pair[1]])
						Glist[-1].extend(zero4)
					Glist[-1].extend(zero8)
					for ls in Glist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'H':
					ind1 = mlist2.index(pair)
					posh.pop(pair[1]-1)
					posh.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Hlist):
						Hlist.append([pair[1]])
						Hlist[-1].extend(zero4)
					Hlist[-1].extend(zero8)
					for ls in Hlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'4':
					ind1 = mlist2.index(pair)
					pos4.pop(pair[1]-1)
					pos4.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(THlist):
						THlist.append([pair[1]])
						THlist[-1].extend(zero4)
					THlist[-1].extend(zero8)
					for ls in THlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'3':
					ind1 = mlist2.index(pair)
					pos3.pop(pair[1]-1)
					pos3.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(RDlist):
						RDlist.append([pair[1]])
						RDlist[-1].extend(zero4)
					RDlist[-1].extend(zero8)
					for ls in RDlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'2':
					ind1 = mlist2.index(pair)
					pos2.pop(pair[1]-1)
					pos2.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(NDlist):
						NDlist.append([pair[1]])
						NDlist[-1].extend(zero4)
					NDlist[-1].extend(zero8)
					for ls in NDlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

				elif pair[0] == u'1':
					ind1 = mlist2.index(pair)
					pos1.pop(pair[1]-1)
					pos1.insert(pair[1]-1, float(str(wlist2[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(STlist):
						STlist.append([pair[1]])
						STlist[-1].extend(zero4)
					STlist[-1].extend(zero8)
					for ls in STlist:
						if pair[1] == ls[0]:
							if 100 > wlist2[ind]:
								ls[5] = ls[5] + 1
							elif 100 <= wlist2[ind] and wlist2[ind] < 400:
								ls[6] = ls[6] + 1
							elif 400 <= wlist2[ind] and wlist2[ind] < 700:
								ls[7] = ls[7] + 1
							elif 700 <= wlist2[ind] or loss < wlist2[ind] or wlist2[ind] == initial_weight2:
								ls[8] = ls[8] + 1

# FROM CLAMPLIFT #
		if cpcode != "" and cwidth != "":
			query3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).values_list('id')
			qexists3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).exists()

			if qexists3 == True:
				delist3 = list()
				wlist3 = list()
				ridlist3 = list()
				elist3 = list()

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
					for totem in delist3:
						totem.append(weight)

				initial_weight3 = int(str(PaperRoll.objects.filter(paper_code=cpcode).values_list('initial_weight')[0])[1:][:-3])

			mquery3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).values_list('lane', 'position')
			mexists3 = PaperRoll.objects.filter(paper_code=cpcode, width=cwidth).exists()
			mstr3 = str(mquery3)
			mlist3 = list(mquery3)

			for ind,pair in enumerate(mlist3):
				if pair[0] == u'A':
					ind1 = mlist3.index(pair)
					posa.pop(pair[1]-1)
					posa.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Alist):
						Alist.append([pair[1]])
						Alist[-1].extend(zero8)
					Alist[-1].extend(zero12)
					for ls in Alist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'B':
					ind1 = mlist3.index(pair)
					posb.pop(pair[1]-1)
					posb.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Blist):
						Blist.append([pair[1]])
						Blist[-1].extend(zero8)
					Blist[-1].extend(zero12)
					for ls in Blist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'C':
					ind1 = mlist3.index(pair)
					posc.pop(pair[1]-1)
					posc.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Clist):
						Clist.append([pair[1]])
						Clist[-1].extend(zero8)
					Clist[-1].extend(zero12)
					for ls in Clist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'D':
					ind1 = mlist3.index(pair)
					posd.pop(pair[1]-1)
					posd.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Dlist):
						Dlist.append([pair[1]])
						Dlist[-1].extend(zero8)
					Dlist[-1].extend(zero12)
					for ls in Dlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'E':
					ind1 = mlist3.index(pair)
					pose.pop(pair[1]-1)
					pose.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Elist):
						Elist.append([pair[1]])
						Elist[-1].extend(zero8)
					Elist[-1].extend(zero12)
					for ls in Elist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'F':
					ind1 = mlist3.index(pair)
					posf.pop(pair[1]-1)
					posf.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Flist):
						Flist.append([pair[1]])
						Flist[-1].extend(zero8)
					Flist[-1].extend(zero12)
					for ls in Flist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'G':
					ind1 = mlist3.index(pair)
					posg.pop(pair[1]-1)
					posg.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Glist):
						Glist.append([pair[1]])
						Glist[-1].extend(zero8)
					Glist[-1].extend(zero12)
					for ls in Glist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'H':
					ind1 = mlist3.index(pair)
					posh.pop(pair[1]-1)
					posh.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Hlist):
						Hlist.append([pair[1]])
						Hlist[-1].extend(zero8)
					Hlist[-1].extend(zero12)
					for ls in Hlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'4':
					ind1 = mlist3.index(pair)
					pos4.pop(pair[1]-1)
					pos4.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(THlist):
						THlist.append([pair[1]])
						THlist[-1].extend(zero4)
					THlist[-1].extend(zero8)
					for ls in THlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'3':
					ind1 = mlist3.index(pair)
					pos3.pop(pair[1]-1)
					pos3.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(RDlist):
						RDlist.append([pair[1]])
						RDlist[-1].extend(zero4)
					RDlist[-1].extend(zero8)
					for ls in RDlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'2':
					ind1 = mlist3.index(pair)
					pos2.pop(pair[1]-1)
					pos2.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(NDlist):
						NDlist.append([pair[1]])
						NDlist[-1].extend(zero4)
					NDlist[-1].extend(zero8)
					for ls in NDlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

				elif pair[0] == u'1':
					ind1 = mlist3.index(pair)
					pos1.pop(pair[1]-1)
					pos1.insert(pair[1]-1, float(str(wlist3[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(STlist):
						STlist.append([pair[1]])
						STlist[-1].extend(zero4)
					STlist[-1].extend(zero8)
					for ls in STlist:
						if pair[1] == ls[0]:
							if 100 > wlist3[ind]:
								ls[9] = ls[9] + 1
							elif 100 <= wlist3[ind] and wlist3[ind] < 400:
								ls[10] = ls[10] + 1
							elif 400 <= wlist3[ind] and wlist3[ind] < 700:
								ls[11] = ls[11] + 1
							elif 700 <= wlist3[ind] or loss < wlist3[ind] or wlist3[ind] == initial_weight3:
								ls[12] = ls[12] + 1

# FROM PLAN #
		if pcode != "" and width != "":
			query = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('id')
			qexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()

			if qexists == True:
				delist = list()
				wlist = list()
				ridlist = list()
				elist = list()

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
					for totem in delist:
						totem.append(weight)

				initial_weight = int(str(PaperRoll.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])

			mquery = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('lane', 'position')
			mexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()
			mstr = str(mquery)
			mlist = list(mquery)

			for ind,pair in enumerate(mlist):
				if pair[0] == u'A':
					ind1 = mlist.index(pair)
					posa.pop(pair[1]-1)
					posa.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Alist):
						Alist.append([pair[1]])
						Alist[-1].extend(zero4)
					for ls in Alist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'B':
					ind1 = mlist.index(pair)
					posb.pop(pair[1]-1)
					posb.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Blist):
						Blist.append([pair[1]])
						Blist[-1].extend(zero12)
					for ls in Blist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'C':
					ind1 = mlist.index(pair)
					posc.pop(pair[1]-1)
					posc.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Clist):
						Clist.append([pair[1]])
						Clist[-1].extend(zero4)
					for ls in Clist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'D':
					ind1 = mlist.index(pair)
					posd.pop(pair[1]-1)
					posd.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Dlist):
						Dlist.append([pair[1]])
						Dlist[-1].extend(zero4)
					for ls in Dlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'E':
					ind1 = mlist.index(pair)
					pose.pop(pair[1]-1)
					pose.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Elist):
						Elist.append([pair[1]])
						Elist[-1].extend(zero4)
					for ls in Elist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'F':
					ind1 = mlist.index(pair)
					posf.pop(pair[1]-1)
					posf.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Flist):
						Flist.append([pair[1]])
						Flist[-1].extend(zero4)
					for ls in Flist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'G':
					ind1 = mlist.index(pair)
					posg.pop(pair[1]-1)
					posg.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Glist):
						Glist.append([pair[1]])
						Glist[-1].extend(zero4)
					for ls in Glist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'H':
					ind1 = mlist.index(pair)
					posh.pop(pair[1]-1)
					posh.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(Hlist):
						Hlist.append([pair[1]])
						Hlist[-1].extend(zero4)
					for ls in Hlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'4':
					ind1 = mlist.index(pair)
					pos4.pop(pair[1]-1)
					pos4.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(THlist):
						THlist.append([pair[1]])
						THlist[-1].extend(zero4)
					THlist[-1].extend(zero8)
					for ls in THlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'3':
					ind1 = mlist.index(pair)
					pos3.pop(pair[1]-1)
					pos3.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(RDlist):
						RDlist.append([pair[1]])
						RDlist[-1].extend(zero4)
					RDlist[-1].extend(zero8)
					for ls in RDlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'2':
					ind1 = mlist.index(pair)
					pos2.pop(pair[1]-1)
					pos2.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(NDlist):
						NDlist.append([pair[1]])
						NDlist[-1].extend(zero4)
					NDlist[-1].extend(zero8)
					for ls in NDlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

				elif pair[0] == u'1':
					ind1 = mlist.index(pair)
					pos1.pop(pair[1]-1)
					pos1.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
					if str(pair[1]) not in str(STlist):
						STlist.append([pair[1]])
						STlist[-1].extend(zero4)
					STlist[-1].extend(zero8)
					for ls in STlist:
						if pair[1] == ls[0]:
							if 100 > wlist[ind]:
								ls[1] = ls[1] + 1
							elif 100 <= wlist[ind] and wlist[ind] < 400:
								ls[2] = ls[2] + 1
							elif 400 <= wlist[ind] and wlist[ind] < 700:
								ls[3] = ls[3] + 1
							elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
								ls[4] = ls[4] + 1

		for ind,item in enumerate(pos1):
			if item == atposition:
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
			if item == atposition:
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
			if item == atposition:
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
			if item == atposition:
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

#		if lane == 'A' or lane == 'B' or lane == '1': lane = '1'
#		if lane == 'C' or lane == 'D' or lane == '2': lane = '2'
#		if lane == 'E' or lane == 'F' or lane == '3': lane = '3'
#		if lane == 'G' or lane == 'H' or lane == '4': lane = '4'

#		if clamping == "yes" and changed == "no":
#			query2 = PaperRoll.objects.filter(id=realtag).values_list('paper_code', 'width', 'wunit', 'initial_weight', 'temp_weight')[0]
#			qlist = list(query2)
#			paper_code = qlist[0]
#			wize = qlist[1]
#			wunit = qlist[2]
#			initial_weight = qlist[3]
#			temp_weight = qlist[4]
#			p = PaperRoll(id=realtag, width=wize, wunit=wunit, initial_weight=initial_weight, temp_weight=temp_weight)
#			p.paper_code = paper_code
#			p.width = wize
#			p.wunit = wunit
#			p.initial_weight = initial_weight
#			p.temp_weight = temp_weight
#			p.lane = atlane
#			p.position = atposition
#			p.save()

	except:
		pass

	return render_to_response('inventory.html', locals())
