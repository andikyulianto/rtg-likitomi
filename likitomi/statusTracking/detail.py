#Author: Chanaphan Prasomwong
# Last updated: 11/1/2010 
# Purpose: this file is containing function
# for displaying the detail contents
# most of the functions are for PC 
# which they are view each department without
# recordable access

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from statusTracking.utility import todayDate, currentTimeProcess, currentProcess
from statusTracking.models import Employee, FakeStatusTracking

##################################################
##         initialize the page settings         ##
## this function for pc to entering view access ##
##################################################
def pcdetail(request):
	eID = request.GET['eID']
	page =request.GET['page']
	today = todayDate()
	title = str(today)
	is_enable_table = True
	is_enable_desktop = True
	employee = Employee.objects.get(eid=eID)
	section_title = "Homepage for " + page + " Login as " + employee.firstname + " " + employee.lastname
	if(page == "CR"):
		return showCR(eID,section_title)	
	if(page == "CV"):
		return showCV(eID,section_title)
	if(page == "PT"):
		return showPT(eID,section_title)
	if(page == "WH"):
		return showWH(eID,section_title)
	return render_to_response('home.html', locals())

#################################
##            for CR           ##
## display only today schedule ##
#################################
def showCR(eid,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View corrugator plan"
	eID = eid
	#create items for CR
	cr = str(currentProcess("CR"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	items = list(item_plan)
	return render_to_response('PC/CR.html', locals())
#################################
##            for CV           ##
## display only today schedule ##
#################################
def showCV(eid,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View convertor plan"
	eID = eid
	#create items for CV
	cvThreeCL = str(currentProcess("3CL"))[2:8]
	cvTwoCL = str(currentProcess("2CL"))[2:8]
	cvThreeCS = str(currentProcess("3CS"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "process1","process3","process4").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('PC/CV.html', locals())
#################################
##            for PT           ##
## display only today schedule ##
#################################
def showPT(eid,section_title):
	eID = eid
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View Pad and Partition"
	#create items for PT
	today = todayDate()
	pt = str(currentTimeProcess("PT"))
	item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end","process2","process4").order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('PC/PT.html', locals())
#################################
##            for WH           ##
## display only today schedule ##
#################################
def showWH(eid,section_title):
	eID = eid
	title = "View Warehouse"
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today = todayDate()
	#create items for WH
	wh = currentTimeProcess("WH")
	item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_id","plan_wh_start", "product_id","actual_wh_start","process1","process2","process3").order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('PC/WH.html',locals())
