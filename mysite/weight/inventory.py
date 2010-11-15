# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction

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

		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
		cur = conn.cursor()

		cur.execute("SELECT DISTINCT `paper_code`, `size` FROM `paper_rolldetails` WHERE `paper_code` = %s", pcode)
		query = cur.fetchall()

		delist = list()
		qidlist = list()
		maplist = list()

		for item in query:
			totem = list(item)
			delist.append(totem)
			paper_code = totem[0]
			size = totem[1]
#			paper_code = 'HAC155'
#			size = 64

#			cur.execute("SELECT COUNT(*) FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
			cur.execute("SELECT `paper_code`, `size` FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
			qroll = cur.fetchall()
			rolls = len(qroll)
			for totem in delist:
				totem.append(rolls)

			cur.execute("SELECT `paper_roll_detail_id` FROM `paper_rolldetails` WHERE `paper_code` = %s AND `size` = %s", (paper_code, size))
			qid = cur.fetchall()
			sum_wt = 0
			for ids in qid:
				ids = str(ids)[1:][:-3]
				qidlist.append(ids)
				cur.execute("SELECT `actual_wt` FROM `paper_movement` WHERE `roll_id` = %s ORDER BY `created_on` DESC", ids)
				only = cur.fetchall()
				if len(only) > 0:
					actual_wt = only[0]
				else:
					cur.execute("SELECT `initial_weight` FROM `paper_rolldetails` WHERE `paper_roll_detail_id` = %s", ids)
					actual_wt = cur.fetchall()[0]
				factual_wt = float(str(actual_wt)[1:][:-3])
				sum_wt = sum_wt + factual_wt
			for totem in delist:
				totem.append(sum_wt)

		for ids in qidlist:
			cur.execute("SELECT `lane`, `position` FROM `paper_rolldetails` WHERE `paper_roll_detail_id` = %s", ids)
			qloc = cur.fetchall()
			for mapping in qloc:
				maplist.append(mapping)

		lane = ['A','','B','C','','D','E','','F','G','','H']
#		num = range(1,44)
		num = range(1,16)
		position = list()
		for n in num:
			position.append(str(n))
		lanelist = list()
		poslist = list()
		for match in maplist:
			lanelist.append(match[0])
			poslist.append(match[1])

		cur.close()
		conn.close()

	except:
		pass

	return render_to_response('inventory.html', locals())

