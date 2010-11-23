# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRoll, PaperHistory

import datetime
import serial
import MySQLdb
import Image
import socket
import StringIO
import cStringIO
import random

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

#		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
#		cur = conn.cursor()

#		cur.execute("SELECT DISTINCT `paper_code`, `size` FROM `paper_rolldetails` WHERE `paper_code` = %s", pcode)
#		query = cur.fetchall()

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

#		ls = str(query)[2:][:-4].split("L,), (")
#		for rid in ls:
#			exist = PaperHistory.objects.filter(roll_id=rid)
			exists = PaperHistory.objects.filter(roll_id=rid).exists()
			elist.append(exists)
			if exists == True:
				weight = int(str(PaperHistory.objects.filter(roll_id=rid).order_by('-timestamp').values_list('last_wt')[0])[1:][:-3])
			else:
				weight = int(str(PaperRoll.objects.filter(id=rid).values_list('initial_weight')[0])[1:][:-3])
			wlist.append(weight)
			for totem in delist:
				totem.append(weight)

#		for totem in delist:
#			for wt in wlist:
#				totem.append(wt)

		initial_weight = int(str(PaperRoll.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])

#		delist = list()
#		qidlist = list()
#		maplist = list()

#		for item in query:
#			totem = list(item)
#			delist.append(totem)
#			paper_code = totem[0]
#			size = totem[1]
##			paper_code = 'HAC155'
##			size = 64

##			cur.execute("SELECT COUNT(*) FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
#			cur.execute("SELECT `paper_code`, `size` FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
#			qroll = cur.fetchall()
#			rolls = len(qroll)
#			for totem in delist:
#				totem.append(rolls)

#			cur.execute("SELECT `paper_roll_detail_id` FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
#			qid = cur.fetchall()
#			sum_wt = 0
#			for ids in qid:
#				ids = str(ids)[1:][:-3]
#				qidlist.append(ids)
#				cur.execute("SELECT `actual_wt` FROM `paper_movement` WHERE `roll_id` = %s ORDER BY `created_on` DESC", ids)
#				only = cur.fetchall()
#				if len(only) > 0:
#					actual_wt = only[0]
#				else:
#					cur.execute("SELECT `initial_weight` FROM `paper_rolldetails` WHERE `paper_roll_detail_id` = %s", ids)
#					actual_wt = cur.fetchall()[0]
#				factual_wt = float(str(actual_wt)[1:][:-3])
#				sum_wt = sum_wt + factual_wt
#			for totem in delist:
#				totem.append(sum_wt)

#		for ids in qidlist:
#			cur.execute("SELECT `lane`, `position` FROM `paper_rolldetails` WHERE `paper_roll_detail_id` = %s", ids)
#			qloc = cur.fetchall()
#			for mapping in qloc:
#				maplist.append(mapping)

#		posa = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#		posb = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#		posc = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#		posd = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
#		pose = ['1','2','3','4','5','6','7','8','9','10','11','12','13']
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
				posa.remove(str(pair[1]))
				posa.insert(pair[1]-1, wlist[ind1])

		for pair in mlist:
			if pair[0] == u'B':
				ind1 = mlist.index(pair)
				posb.remove(str(pair[1]))
				posb.insert(pair[1]-1, wlist[ind1])

		for pair in mlist:
			if pair[0] == u'C':
				ind1 = mlist.index(pair)
				posc.remove(str(pair[1]))
				posc.insert(pair[1]-1, wlist[ind1])

		for pair in mlist:
			if pair[0] == u'D':
				ind1 = mlist.index(pair)
				posd.remove(str(pair[1]))
				posd.insert(pair[1]-1, wlist[ind1])

		for pair in mlist:
			if pair[0] == u'E':
				ind1 = mlist.index(pair)
				pose.remove(str(pair[1]))
				pose.insert(pair[1]-1, wlist[ind1])

#		num = range(1,44)
#		num = range(1,16)
#		position = list()

#		for n in num:
#			position.append(str(n))
#		lanelist = list()
#		poslist = list()
#		for match in maplist:
#			lanelist.append(match[0])
#			poslist.append(match[1])
#		strlist = str(maplist)

#		cur.close()
#		conn.close()

	except:
		pass

	return render_to_response('inventory.html', locals())

