# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import TblClamplift
from datetime import date, time, datetime, timedelta

def showplan(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	if opdate: 
		query = TblClamplift.objects.filter(opdate=opdate).values_list('start_time', 'product_code', 'p_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'used_df_mkg', 'used_bl_mkg', 'used_bm_mkg', 'used_cl_mkg', 'used_cm_mkg')

	now = datetime.now()
	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('showplan.html', locals())

def required(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	required = TblClamplift.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'flute', 'df', 'bl', 'bm', 'cl', 'cm', 'paper_width_mm', 'paper_width_inch', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	now = datetime.now()
	qlist = list(required)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('required.html', locals())

def detail(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	detail = TblClamplift.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'customer_name', 'product', 'length_df', 'length_bl', 'length_bm', 'length_cl', 'length_cm', 'actual_df', 'actual_bl', 'actual_bm', 'actual_cl', 'actual_cm', 'sheet_length', 'case', 'cut')

	now = datetime.now()
	qlist = list(detail)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('detail.html', locals())
