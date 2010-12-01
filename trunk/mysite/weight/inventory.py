# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRoll, PaperHistory

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
		atposition = '3'
		atlocation = 'Stock'

		realtag = 67

		vlane = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

		for p in vlane:
			if p == atposition:
				ind = vlane.index(p)
				vlane.remove(p)
				vlane.insert(ind, '*')

		if atlane == '1':
			leftlane = 'A'
			rightlane = 'B'
		if atlane == '2':
			leftlane = 'B'
			rightlane = 'C'
		if atlane == '3':
			leftlane = 'C'
			rightlane = 'D'

		if atlane == '4':
			leftlane = 'D'
			rightlane = 'E'

		lane = ['A','','B','','C','','D','','E']
		posall = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
		posa = ['','','3','4','5','6','','8','9','','','','']
		posb = ['','','3','4','5','6','','8','9','','','','']
		posc = ['','','3','4','5','6','','8','9','','','','']
		posd = ['1','2','3','4','5','6','','8','9','10','11','12','13']
		pose = list()
		num = range(1,14)
		for n in num:
			pose.append(str(n))
		mquery = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('lane', 'position')
		mstr = str(mquery)
		mlist = list(mquery)

		for pair in mlist:
			if pair[0] == u'A':
				ind1 = mlist.index(pair)
				posa.pop(pair[1]-1)
				posa.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))

			elif pair[0] == u'B':
				ind1 = mlist.index(pair)
				posb.pop(pair[1]-1)
				posb.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))

			elif pair[0] == u'C':
				ind1 = mlist.index(pair)
				posc.pop(pair[1]-1)
				posc.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))

			elif pair[0] == u'D':
				ind1 = mlist.index(pair)
				posd.pop(pair[1]-1)
				posd.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))

			elif pair[0] == u'E':
				ind1 = mlist.index(pair)
				pose.pop(pair[1]-1)
				pose.insert(pair[1]-1, float(str(wlist[ind1])+"."+str(pair[1])))

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

