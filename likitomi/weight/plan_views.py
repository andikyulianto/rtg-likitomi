# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import ClampliftPlan, PaperRoll, PaperHistory
from datetime import date

def plan(request):
	try:
		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT date
			FROM weight_clampliftplan
			ORDER BY date DESC""")
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

		if 'opdate' in request.GET and request.GET['opdate']:
			opdate = request.GET['opdate']
		else:
			opdate = ""

	except:
		pass

	return render_to_response('plan.html', locals())

def wholeplan(request):
	try:
		if 'opdate' in request.GET and request.GET['opdate']:
			opdate = request.GET['opdate']
		else:
			opdate = ""

		cursor = connection.cursor()
		cursor.execute("""
			SELECT DISTINCT date
			FROM weight_clampliftplan
			ORDER BY date DESC""")
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
