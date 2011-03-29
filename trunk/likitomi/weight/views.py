# Create your views here.
#from django.template.loader import get_template
from django.shortcuts import render_to_response
#from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan, PaperRoll, PaperHistory

#import datetime
#import serial
#import MySQLdb
#import Image
#import socket
#import StringIO
#import cStringIO
#import random

def index(request):
	try:

# GET values #
		if 'opdate' in request.GET and request.GET['opdate']:
			opdate = request.GET['opdate']
		else:
			opdate = ""

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

		if 'clamping' in request.GET and request.GET['clamping']:
			clamping = request.GET['clamping']
		else:
			clamping = "no"

		if 'changed' in request.GET and request.GET['changed']:
			changed = request.GET['changed']
		else:
			changed = "no"

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



	except:
		pass

	return render_to_response('index.html', locals())

