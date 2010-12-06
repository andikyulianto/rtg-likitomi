# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from mysite.weight.models import PaperRoll, PaperHistory

import socket

def inventory(request):
	try:
		if 'pcode' in request.GET and request.GET['pcode']:
			pcode = request.GET['pcode']
		else:
			return HttpResponseRedirect('/inventory/')

		if 'width' in request.GET and request.GET['width']:
			width = request.GET['width']
		else:
			return HttpResponseRedirect('/inventory/')

		if 'loss' in request.GET and request.GET['loss']:
			loss = request.GET['loss']
		else:
			return HttpResponseRedirect('/inventory/')

		query = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('id')
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

#		for w in wlist:
#			if 100 > w:
#				redlist.append("r")
#			elif 100 <= w and w < 400:
#				yellowlist.append("y")
#			elif 400 <= w and w < 700:
#				bluelist.append("b")
#			elif 700 <= w or loss < w or w == initial_weight:
#				greenlist.append("g")
#		rlen = len(redlist)
#		ylen = len(yellowlist)
#		blen = len(bluelist)
#		glen = len(greenlist)

#		HOST = '192.41.170.55' # CSIM network
#		HOST = '192.168.101.55' # Likitomi network
#		HOST = '192.168.1.55' # My own local network: Linksys
#		PORT = 50007
#		soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#		soc.settimeout(2)
#		soc.connect((HOST, PORT))
#		## soc.send('setup.operating_mode = standby\r\n')
#		soc.send('tag.db.scan_tags(1000)\r\n')
#		datum = soc.recv(128)

#		if datum.find("ok") > -1:
#			soc.send('tag.read_id()\r\n')
#			data = soc.recv(8192)
#			tagdata = data.split("\r\n")

#		idlist = list()
#		loclist = list()

#		for tag in tagdata:
#			if "AAAA" in tag:
#				idlist.append(tag)
#			if "BBBB" in tag:
#				loclist.append(tag)

#		cnt = 0
#		## error = cStringIO.StringIO()

#		tagid_A = list()
#		type_A = list()
#		antenna_A = list()
#		repeat_A = list()

#		for id1 in idlist:
#			id2 = id1.replace("(","")
#			id2 = id2.replace(")","")
#			id3 = id2.split(", ")
#			for id4 in id3:
#				id5 = id4.split("=")
#				if id5[0]=="tag_id":tagid_A.append(id5[1])
#				elif id5[0]=="type":type_A.append(id5[1])
#				elif id5[0]=="antenna": antenna_A.append(id5[1])
#				elif id5[0]=="repeat": repeat_A.append(id5[1])
#				cnt= cnt+1

#		tagid_B = list()
#		type_B = list()
#		antenna_B = list()
#		repeat_B = list()

#		for loc1 in loclist:
#			loc2 = loc1.replace("(","")
#			loc2 = loc2.replace(")","")
#			loc3 = loc2.split(", ")
#			for loc4 in loc3 :
#				loc5 = loc4.split("=")
#				if loc5[0]=="tag_id": tagid_B.append(loc5[1])
#				elif loc5[0]=="type": type_B.append(loc5[1])
#				elif loc5[0]=="antenna": antenna_B.append(loc5[1])
#				elif loc5[0]=="repeat": repeat_B.append(loc5[1])
#				cnt= cnt+1

#		lan = 0
#		pos = 0
#		totalCount = 0

#		if len(repeat_B) > 0 :
#			cnt = 0
#			for rep in repeat_B:
#				if type_B[cnt] == "ISOC":
#					lindex = int(tagid_B[cnt][26:28])
#					pindex = int(tagid_B[cnt][28:30])
#					lan += float(lindex)*float(repeat_B[cnt])
#					pos += float(pindex)*float(repeat_B[cnt])
#					totalCount += float(repeat_B[cnt])

#				cnt = cnt+1

#		if totalCount > 0:
#			L = int(round(lan/totalCount,0))
#			P = int(round(pos/totalCount,0))
#		else:
#			L = 0
#			P = 0

#		atlane = str(L)
#		atposition = str(P)
#		atlocation = ''

#		if L == 0:
#			atlocation = 'CR'
#		if L == 5 and P == 5:
#			atlocation = 'Scale'
#		if L in range(1, 5):
#			atlocation = 'Stock'

#		if L == 0 and P == 0:
#			atlane = ""
#			atposition = ""
#			atlocation = ""
#			toperror = "[No location tag in field.]"

#		repeat_AA = list()

#		for rep_A in repeat_A:
#			repeat_AA.append(int(rep_A))

#		if max(repeat_AA) in repeat_AA:
#			n = repeat_AA.index(max(repeat_AA))

#		tagsplt = tagid_A[n].split("AAAA")
#		realtag = int(tagsplt[1][0:4])

#		soc.close()

#		atlane = '5'
#		atposition = '5'
#		atlocation = 'Scale'

		atlane = '1'
		atposition = '8'
		atlocation = 'Stock'

		realtag = 67

		vlane = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

		for p in vlane:
			if p == atposition:
				ind = vlane.index(p)
				vlane.remove(p)
				vlane.insert(ind, '*')

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

#		lane = ['A','','B','','C','','D','','E']
#		posall = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#		posa = ['','','3','4','5','6','','8','9','','','','']
#		posb = ['','','3','4','5','6','','8','9','','','','']
#		posc = ['','','3','4','5','6','','8','9','','','','']
#		posd = ['1','2','3','4','5','6','','8','9','10','11','12','13']
#		pose = list()
#		num = range(1,14)
#		for n in num:
#			pose.append(str(n))

		lane = ['H','','G','F','','E','D','','C','B','','A']
		posall = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
		posh = ['','','3','4','5','6','','8','9','','','','']
		posg = ['','','3','4','5','6','','8','9','','','','']
		posf = ['','','3','4','5','6','','8','9','','','','']
		pose = ['','','3','4','5','6','','8','9','','','','']
		posd = ['','','3','4','5','6','','8','9','','','','']
		posc = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		posb = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		posa = ['1','2','3','4','5','6','7','8','9','10','11','12','13']

		mquery = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('lane', 'position')
		mstr = str(mquery)
		mlist = list(mquery)

#		redlistA = list()
#		yellowlistA = list()
#		bluelistA = list()
#		greenlistA = list()
#		wlistA = list()

#		redlistB = list()
#		yellowlistB = list()
#		bluelistB = list()
#		greenlistB = list()
#		wlistB = list()

		Alist = list()
		Blist = list()
		Clist = list()
		Dlist = list()
		Elist = list()
		Flist = list()
		Glist = list()
		Hlist = list()

		zero = [0, 0, 0, 0]
#		rlenA = 0
#		ylenA = 0
#		blenA = 0
#		glenA = 0

#		mylist = [ind for ind,pair in enumerate(mlist) if pair[0] == u'A']
		for ind,pair in enumerate(mlist):
			if pair[0] == u'A':
				ind1 = mlist.index(pair)
				posa.pop(pair[1]-1)
				posa.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
				if str(pair[1]) not in str(Alist):
					Alist.append([pair[1]])
					Alist[-1].extend(zero)
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

#				rlenA = 0
#				ylenA = 0
#				blenA = 0
#				glenA = 0
#				if 100 > wlist[ind]:
#					rlenA = rlenA + 1
#				elif 100 <= wlist[ind] and wlist[ind] < 400:
#					ylenA = ylenA + 1
#				elif 400 <= wlist[ind] and wlist[ind] < 700:
#					blenA = blenA + 1
#				elif 700 <= wlist[ind] or loss < wlist[ind] or wlist[ind] == initial_weight:
#					glenA = glenA + 1

#				Alist[ind].append(rlenA)
#				Alist[ind].append(ylenA)
#				Alist[ind].append(blenA)
#				Alist[ind].append(glenA)

#				for i,x in enumerate(mlist):
#					if x == pair:
#						if 100 > wlist[i]:
#							rlenA = rlenA + 1
#						elif 100 <= wlist[i] and wlist[i] < 400:
#							ylenA = ylenA + 1
#						elif 400 <= wlist[i] and wlist[i] < 700:
#							blenA = blenA + 1
#						elif 700 <= wlist[i] or loss < wlist[i] or wlist[i] == initial_weight:
#							glenA = glenA + 1
#				if str(pair[1]) not in str(Alist):
#					Alist.append([pair[1]])
#					Alist[ind1].append(rlenA)
#					Alist[ind1].append(ylenA)
#					Alist[ind1].append(blenA)
#					Alist[ind1].append(glenA)

#				Alist[ind1].append(rlenA)
#				Alist[ind1].append(ylenA)
#				Alist[ind1].append(blenA)
#				Alist[ind1].append(glenA)

			elif pair[0] == u'B':
				ind1 = mlist.index(pair)
				posb.pop(pair[1]-1)
				posb.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
				if str(pair[1]) not in str(Blist):
					Blist.append([pair[1]])
					Blist[-1].extend(zero)
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
					Clist[-1].extend(zero)
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
					Dlist[-1].extend(zero)
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
					Elist[-1].extend(zero)
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
				posc.pop(pair[1]-1)
				posc.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
				if str(pair[1]) not in str(Flist):
					Flist.append([pair[1]])
					Flist[-1].extend(zero)
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
				posd.pop(pair[1]-1)
				posd.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
				if str(pair[1]) not in str(Glist):
					Glist.append([pair[1]])
					Glist[-1].extend(zero)
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
				pose.pop(pair[1]-1)
				pose.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
				if str(pair[1]) not in str(Hlist):
					Hlist.append([pair[1]])
					Hlist[-1].extend(zero)
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

#		for match in Alist:
#			if match[0] == match[0]:
#				match.remove(match[0])

#		for w in wlistA:
#			if 100 > w:
#				redlistA.append("rA")
#			elif 100 <= w and w < 400:
#				yellowlistA.append("yA")
#			elif 400 <= w and w < 700:
#				bluelistA.append("bA")
#			elif 700 <= w or loss < w or w == initial_weight:
#				greenlistA.append("gA")
#		rlenA = len(redlistA)
#		ylenA = len(yellowlistA)
#		blenA = len(bluelistA)
#		glenA = len(greenlistA)
#		for ls in Alist:
#			ls.append(rlenA)
#			ls.append(ylenA)
#			ls.append(blenA)
#			ls.append(glenA)
#		for w in wlistB:
#			if 100 > w:
#				redlistB.append("rB")
#			elif 100 <= w and w < 400:
#				yellowlistB.append("yB")
#			elif 400 <= w and w < 700:
#				bluelistB.append("bB")
#			elif 700 <= w or loss < w or w == initial_weight:
#				greenlistB.append("gB")
#		rlenB = len(redlistB)
#		ylenB = len(yellowlistB)
#		blenB = len(bluelistB)
#		glenB = len(greenlistB)
#		for ls in Blist:
#			ls.append(rlenB)
#			ls.append(ylenB)
#			ls.append(blenB)
#			ls.append(glenB)

		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT paper_code
			FROM weight_paperroll
			ORDER BY paper_code""")
		qscode = cursor.fetchall()
		scode = list()
		for sc in qscode:
			scode.append(sc[0])
		cursor.execute("""
			SELECT DISTINCT width
			FROM weight_paperroll
			ORDER BY width""")
		qswidth = cursor.fetchall()
		swidth = list()
		for sw in qswidth:
			swidth.append(sw[0])

	except:
		pass

	return render_to_response('inventory.html', locals())

