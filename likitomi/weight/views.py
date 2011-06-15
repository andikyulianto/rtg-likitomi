# Create your views here.
#from django.template.loader import get_template
#from django.template import Template, Context
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction
#import serial
#import MySQLdb
#import Image
#import socket
#import StringIO
#import cStringIO
#import random
#from datetime import datetime
from weight.models import ClampliftPlan, PaperRoll, PaperHistory

def dashboard(request):

# Query date list for plan #
	dcursor = connection.cursor()
	dcursor.execute("""
		SELECT DISTINCT date
		FROM weight_clampliftplan
		ORDER BY date DESC""")
	dquery = dcursor.fetchall()
	dlen = len(dquery)
	if len(dquery) == 1:
		dstr = str(dquery)[16:][:-5]
	else:
		dstr = str(dquery)[16:][:-4]
	dsplt = dstr.split('),), (datetime.date(')
	datelist = list()
	for date in dsplt:
		datefrm = date.replace(", ","-")
		datelist.append(datefrm)

# Query paper code and size for search menu #
	scursor1 = connection.cursor()
	scursor1.execute("""
		SELECT DISTINCT paper_code
		FROM weight_paperroll
		ORDER BY paper_code""")
	spcode = scursor1.fetchall()
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])
	scursor2 = connection.cursor()
	scursor2.execute("""
		SELECT DISTINCT width
		FROM weight_paperroll
		ORDER BY width""")
	swidth = scursor2.fetchall()
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	return render_to_response('dashboard.html', locals())

