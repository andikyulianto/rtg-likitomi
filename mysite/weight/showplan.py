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
#	lstart_time = list()
#	lproduct_code = list()
#	lDF = list()
#	lBL = list()
#	lBM = list()
#	lCL = list()
#	lCM = list()
#	lused_df_mkg = list()
#	lused_bl_mkg = list()
#	lused_bm_mkg = list()
#	lused_cl_mkg = list()
#	lused_cm_mkg = list()

#	for item in query:
#		start_time = item[0]
#		lstart_time.append(start_time)
#		product_code = item[1]
#		lproduct_code.append(product_code)
#		DF = item[2]
#		lDF.append(DF)
#		BL = item[3]
#		lBL.append(BL)
#		BM = item[4]
#		lBM.append(BM)
#		CL = item[5]
#		lCL.append(CL)
#		CM = item[6]
#		lCM.append(CM)
#		used_df_mkg = item[7]
#		lused_df_mkg.append(used_df_mkg)
#		used_bl_mkg = item[8]
#		lused_bl_mkg.append(used_bl_mkg)
#		used_bm_mkg = item[9]
#		lused_bm_mkg.append(used_bm_mkg)
#		used_cl_mkg = item[10]
#		lused_cl_mkg.append(used_cl_mkg)
#		used_cm_mkg = item[11]
#		lused_cm_mkg.append(used_cm_mkg)

	cur.close()
	conn.close()

	return render_to_response('showplan.html', locals())

