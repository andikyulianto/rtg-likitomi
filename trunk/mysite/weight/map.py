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

def stockmap(request):
	try:
		if 'pcode' in request.GET and request.GET['pcode']:
			pcode = request.GET['pcode']
		else:
			return HttpResponseRedirect('/map/')

		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
		cur = conn.cursor()
	
		cur.execute("SELECT `paper_code`,`size`,`total_roll`,`total_weight` FROM `roll_stock` WHERE `paper_code` = %s", pcode)
		query = cur.fetchall()
		lpaper_code = list()
		lsize = list()
		ltotal_roll = list()
		ltotal_weight = list()

		for item in query:
			paper_code = item[0]
			lpaper_code.append(paper_code)
			size = item[1]
			lsize.append(size)
			total_roll = item[2]
			ltotal_roll.append(total_roll)
			total_weight = item[3]
			ltotal_weight.append(total_weight)

		cur.close()
		conn.close()
	except:
		pass

	return render_to_response('map.html', locals())

