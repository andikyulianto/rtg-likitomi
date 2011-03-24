# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction

def stock(request):
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

		if 'opdate' in request.GET and request.GET['opdate']:
			opdate = request.GET['opdate']
		else:
			opdate = ""

		if 'clamping' in request.GET and request.GET['clamping']:
			clamping = request.GET['clamping']
		else:
			clamping = "no"

		if 'changed' in request.GET and request.GET['changed']:
			changed = request.GET['changed']
		else:
			changed = "no"

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

	return render_to_response('stock.html', locals())

