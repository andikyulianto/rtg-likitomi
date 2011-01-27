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
			pcode = ""

		if 'width' in request.GET and request.GET['width']:
			width = request.GET['width']
		else:
			width = ""

		if 'loss' in request.GET and request.GET['loss']:
			loss = request.GET['loss']
		else:
			loss = ""

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

		operating_mode = 'real' # Operating mode = {'real', 'fake'} #

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
			## error = cStringIO.StringIO()

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

			if P >= 1 and P <= 3: P = 1
			if P >= 4 and P <= 6: P = 2
			if P >= 7 and P <= 9: P = 3
			if P >= 10 and P <= 12: P = 4
			if P >= 13 and P <= 15: P = 5
			if P >= 16 and P <= 18: P = 6
			if P >= 19 and P <= 21: P = 7
			if P >= 22 and P <= 24: P = 8
			if P >= 25 and P <= 27: P = 9
			if P >= 28 and P <= 30: P = 10
			if P >= 31 and P <= 33: P = 11
			if P >= 34 and P <= 36: P = 12
			if P >= 37: P = 13
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

#			repeat_AA = list()

#			for rep_A in repeat_A:
#				repeat_AA.append(int(rep_A))

#			if max(repeat_AA) in repeat_AA:
#				n = repeat_AA.index(max(repeat_AA))

#			tagsplt = tagid_A[n].split("AAAA")
#			realtag = int(tagsplt[1][0:4])
#			realtag = tagid_A[n][7:11]

			soc.close()

		if operating_mode == 'fake':

			atlane = '5'
			atposition = '5'
			atlocation = 'Scale'

			atlane = '1'
			atposition = '5'
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
		mexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()
		mstr = str(mquery)
		mlist = list(mquery)

		Alist = list()
		Blist = list()
		Clist = list()
		Dlist = list()
		Elist = list()
		Flist = list()
		Glist = list()
		Hlist = list()

		zero = [0, 0, 0, 0]

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
				posf.pop(pair[1]-1)
				posf.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
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
				posg.pop(pair[1]-1)
				posg.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
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
				posh.pop(pair[1]-1)
				posh.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))
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

