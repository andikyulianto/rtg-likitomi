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

def showplan(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		return HttpResponseRedirect('/showplan/')

	conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
	cur = conn.cursor()
	
	cur.execute("SELECT `start_time`,`product_code`,`DF`,`BL`,`BM`,`CL`,`CM`,`used_df_mkg`,`used_bl_mkg`,`used_bm_mkg`,`used_cl_mkg`,`used_cm_mkg` FROM `tbl_clamplift` WHERE `opdate` = %s ORDER BY `start_time` ASC", opdate)
	query = cur.fetchall()

	cur.close()
	conn.close()

	return render_to_response('showplan.html', locals())

def showwhole(request):
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		return HttpResponseRedirect('/showplan/')

	conn = MySQLdb.Connect(host="localhost", user="root", passwd="", db="likitomi_v8")
	cur = conn.cursor()
	
	cur.execute("SELECT `start_time`,`stop_time`,`product_code`,`partner_name`,`product_name`,`sales_order`,`autoid`,`flute`,`DF`,`BL`,`BM`,`CL`,`CM`,`p_width_inch`,`p_width_mm`,`used_df`,`used_bl`,`used_bm`,`used_cl`,`used_cm`,`used_df_lkg`,`used_bl_lkg`,`used_bm_lkg`,`used_cl_lkg`,`used_cm_lkg`,`used_df_mkg`,`used_bl_mkg`,`used_bm_mkg`,`used_cl_mkg`,`used_cm_mkg`,`t_length`,`case`,`cut` FROM `tbl_clamplift` WHERE `opdate` = %s ORDER BY `start_time` ASC", opdate)
	query = cur.fetchall()

	cur.close()
	conn.close()

	return render_to_response('showwhole.html', locals())
