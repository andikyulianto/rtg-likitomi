# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from mysite.weight.models import ClampliftPlan
from datetime import date

def showplan(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	query = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'paper_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	return render_to_response('showplan.html', locals())

def showreq(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	return render_to_response('showreq.html', locals())

def reqhead(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	required = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'flute', 'df', 'bl', 'bm', 'cl', 'cm', 'paper_width_mm', 'paper_width_inch', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	return render_to_response('reqhead.html', locals())

def required(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	required = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'flute', 'df', 'bl', 'bm', 'cl', 'cm', 'paper_width_mm', 'paper_width_inch', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	return render_to_response('required.html', locals())



def showdet(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	return render_to_response('showdet.html', locals())

def dethead(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")

	detail = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'customer_name', 'product', 'length_df', 'length_bl', 'length_bm', 'length_cl', 'length_cm', 'actual_df', 'actual_bl', 'actual_bm', 'actual_cl', 'actual_cm', 'sheet_length', 'case', 'cut')

	return render_to_response('dethead.html', locals())

def detail(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today()
		opdate.strftime("%Y-%m-%d")
	detail = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno', 'customer_name', 'product', 'length_df', 'length_bl', 'length_bm', 'length_cl', 'length_cm', 'actual_df', 'actual_bl', 'actual_bm', 'actual_cl', 'actual_cm', 'sheet_length', 'case', 'cut')

	return render_to_response('detail.html', locals())
