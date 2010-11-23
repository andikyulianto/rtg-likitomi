# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan

import datetime
import serial
import MySQLdb
import Image
import socket
import StringIO
import cStringIO
import random

def plan(request):
	try:
#		now = datetime.datetime.now()
#		today = now.strftime("%Y-%m-%d")

#		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
#		cur = conn.cursor()

#		cur.execute("SELECT DISTINCT `opdate` FROM `tbl_clamplift` ORDER BY `opdate` DESC")
#		query = cur.fetchall()
#		qlen = len(query)
#		qstr = str(query)[16:][:-4]
#		qsplt = qstr.split('),), (datetime.date(')
#		datelist = list()
#		for date in qsplt:
#			datefrm = date.replace(", ","-")
#			datelist.append(datefrm)

#		cur.close()
#		conn.close()
		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT date
			FROM weight_clampliftplan""")
		query = cursor.fetchall()

#		query = ClampliftPlan.objects.distinct().values_list('date')
		qlen = len(query)
		if len(query) == 1:
			qstr = str(query)[16:][:-5]
		else:
			qstr = str(query)[16:][:-4]
		qsplt = qstr.split('),), (datetime.date(')
		datelist = list()
		for date in qsplt:
			datefrm = date.replace(", ","-")
			datelist.append(datefrm)

	except:
		pass

	return render_to_response('plan.html', locals())

def wholeplan(request):
	try:
		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT date
			FROM weight_clampliftplan""")
		query = cursor.fetchall()

		qlen = len(query)
		if len(query) == 1:
			qstr = str(query)[16:][:-5]
		else:
			qstr = str(query)[16:][:-4]
		qsplt = qstr.split('),), (datetime.date(')
		datelist = list()
		for date in qsplt:
			datefrm = date.replace(", ","-")
			datelist.append(datefrm)

	except:
		pass

	return render_to_response('wholeplan.html', locals())
