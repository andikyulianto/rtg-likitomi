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

def stock(request):
	try:
		conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
		cur = conn.cursor()

		cur.execute("SELECT DISTINCT `paper_code` FROM `paper_rolldetails`")
		query = cur.fetchall()
		qlen = len(query)
		qstr = str(query)[3:][:-4]
		qsplt = qstr.split("',), ('")
		pcodelist = list()
		for pcode in qsplt:
			pcodelist.append(pcode)

		cur.close()
		conn.close()

	except:
		pass

	return render_to_response('stock.html', locals())

