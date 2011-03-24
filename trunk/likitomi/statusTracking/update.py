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
from django.http import HttpResponseRedirect
from statusTracking.models import Employee, FakeStatusTracking, ProductCatalog, Products

################################################
## this page is will record to starting field ##
################################################
def startUpdate(request):
	current_time = todayDate()
	eID = request.GET['eID']
	task = request.GET['task']
	at = request.GET['at']
	pID = request.GET['pID']
	if(at=="WH"):
		amount = request.GET['amount']
	obj = FakeStatusTracking.objects.get(plan_id=pID)
	if (at=="CR"):
		obj.actual_cr_start = current_time
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="CV"):
		obj.actual_cv_start = current_time
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="PT"):
		obj.actual_pt_start = current_time
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="WH"):
		obj.actual_wh_start = current_time
		obj.actual_amount_wh = amount
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	else:
		return render_to_response('update.html', locals())
	
##############################################
## this page is will record to ending field ##
##############################################
def endUpdate(request):
	current_time = todayDate()
	eID = request.GET['eID']
	task = request.GET['task']
	at = request.GET['at']
	amount = request.GET['amount']
	pID = request.GET['pID']
	obj = FakeStatusTracking.objects.get(plan_id=pID)
	if (at=="CR"):
		obj.actual_cr_end = current_time
		obj.actual_amount_cr = amount
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="CV"):
		obj.actual_cv_end = current_time
		obj.actual_amount_cv = amount
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="PT"):
		obj.actual_pt_end = current_time
		obj.actual_amount_pt = amount
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	elif (at=="WH"):
		obj.actual_wh_start = current_time
		obj.actual_amount_wh = amount
		obj.save()
		path = "/likitomi/home/?eID="+eID+"&Enter=Enter"
		return HttpResponseRedirect(path)
	else:
		return render_to_response('update.html', locals())
