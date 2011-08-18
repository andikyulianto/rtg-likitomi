# Author: Chanaphan Prasomwong
# Last updated: 11/1/2010 
# Purpose: to record the starting and 
# stopping time for each section_title
# this page retreives information 
# and displays to the users before
# saving dirctly into model
# These functions will redirected to previous
# home of each section depending on th users' department'

from django.http import HttpResponse
from django.shortcuts import render_to_response
from statusTracking.utility import todayDate
from statusTracking.config import rootPath
from django.http import HttpResponseRedirect
from statusTracking.models import AuthUser, StatusTracking, ProductCatalog, Products, Delivery
from employee import Employee

################################################
## this page is will record to starting field ##
################################################
def startUpdate(request):
	current_time = todayDate()
	eID = request.GET['eID']

	employee = AuthUser.objects.get(id=eID)
	username = employee.username
	task = request.GET['task']
	at = request.GET['at']
	pID = request.GET['pID']
	if(at=="WH"):
		ref_in = request.GET['ref_in']
	if(at!="CR"):
		amount = request.GET['amount']

	obj = StatusTracking.objects.get(plan_id=pID)
	dl_id = obj.delivery_id
	dl = Delivery.objects.get(delivery_id = dl_id)
	if (at=="CR"):
		obj.actual_cr_start = current_time
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="CV"):
		obj.actual_cv_start = current_time
		obj.actual_amount_cv_in = int(amount)
#		print "amount :"+ amount
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="PT"):
		obj.actual_pt_start = current_time
		obj.actual_amount_pt_in = int(amount)
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="WH"):
		obj.actual_wh_start = current_time
		obj.actual_amount_wh = amount
		dl.doc_ref_in = ref_in
		dl.total_production_qty = amount
		obj.save()
		dl.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	else:
		return render_to_response('update.html', locals())
	
##############################################
## this page is will record to ending field ##
##############################################
def endUpdate(request):
	current_time = todayDate()
	eID = request.GET['eID']
	employee = AuthUser.objects.get(id=eID)
	username = employee.username
	task = request.GET['task']
	at = request.GET['at']
	amount = request.GET['amount']
	if(at=="WH"):
		ref_out = request.GET['ref_out']

	pID = request.GET['pID']
	obj = StatusTracking.objects.get(plan_id=pID)
	dl_id = obj.delivery_id
	dl = Delivery.objects.get(delivery_id = dl_id)
	if (at=="CR"):
		obj.actual_cr_end = current_time
		obj.actual_amount_cr = amount
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="CV"):
		obj.actual_cv_end = current_time
		obj.actual_amount_cv = amount
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="PT"):
		obj.actual_pt_end = current_time
		obj.actual_amount_pt = amount
		obj.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="WH"):
		obj.actual_wh_end = current_time
		obj.actual_amount_wh_out = amount
		dl.doc_ref_out = ref_out
		dl.delivered_qty = amount
		obj.save()
		dl.save()
		path = rootPath()+"/home/?user="+username+"&Enter=Enter#tabs-2"
		return HttpResponseRedirect(path)
	else:
		return render_to_response('update.html', locals())
