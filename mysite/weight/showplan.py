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

def showplan(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		return HttpResponseRedirect('/showplan/')

#	conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
#	cur = conn.cursor()
#	
#	cur.execute("SELECT `start_time`,`product_code`,`DF`,`BL`,`BM`,`CL`,`CM`,`used_df_mkg`,`used_bl_mkg`,`used_bm_mkg`,`used_cl_mkg`,`used_cm_mkg` FROM `tbl_clamplift` WHERE `opdate` = %s ORDER BY `start_time` ASC", opdate)
#	query = cur.fetchall()

#	cur.close()
#	conn.close()

	query = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'paper_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	return render_to_response('showplan.html', locals())

def showwhole(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		return HttpResponseRedirect('/showwhole/')

	always = ClampliftPlan.objects.filter(date=opdate).values_list('start_time', 'sheet_code', 'sono', 'ordno')

	required = ClampliftPlan.objects.filter(date=opdate).values_list('flute', 'df', 'bl', 'bm', 'cl', 'cm', 'paper_width_mm', 'paper_width_inch', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

	return render_to_response('showwhole.html', locals())

def detail(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		return HttpResponseRedirect('/showwhole/')

	detail = ClampliftPlan.objects.filter(date=opdate).values_list('customer_name', 'product', 'length_df', 'length_bl', 'length_bm', 'length_cl', 'length_cm', 'actual_df', 'actual_bl', 'actual_bm', 'actual_cl', 'actual_cm', 'sheet_length', 'case', 'cut')

	return render_to_response('detail.html', locals())