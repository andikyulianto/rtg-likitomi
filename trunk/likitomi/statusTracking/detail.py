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
from statusTracking.models import AuthUser, StatusTracking
from datetime import date, datetime
from employee import Employee
import calendar

##################################################
##         initialize the page settings         ##
## this function for pc to entering view access ##
##################################################
def pcdetail(request):
	user = request.GET['user']
	page =request.GET['page']
	today = todayDate()
	title = str(today)
	is_enable_table = True
	is_enable_desktop = True
	employee = Employee(user)
	section_title = "Homepage for " + page + " Login as " + employee.firstname + " " + employee.lastname
	if(page == "CR"):
		return showCR(user,section_title)	
	if(page == "CV"):
		return showCV(user,section_title)
	if(page == "PT"):
		return showPT(user,section_title)
	if(page == "WH"):
		return showWH(user,section_title)
	return render_to_response('home.html', locals())

#################################
##            for CR           ##
## display only today schedule ##
#################################
def showCR(User,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View corrugator plan"
	page = "CR"
	user = User
	#create items for CR
	cr = str(currentProcess("CR"))
	item_plan = StatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start')
	items = list(item_plan)
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_cr_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsM = list(item_planM)
	return render_to_response('PC/CR.html', locals())
#################################
##            for CV           ##
## display only today schedule ##
#################################
def showCV(User,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View convertor plan"
	user = User
	page = "CV"
	#create items for CV
	cvThreeCL = str(currentProcess("3CL"))[3:9]
	cvTwoCL = str(currentProcess("2CL"))[3:9]
	cvThreeCS = str(currentProcess("3CS"))[3:9]
	item_plan = StatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start')
	items = list(item_plan)
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_cv_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsM = list(item_planM)
	return render_to_response('PC/CV.html', locals())
#################################
##            for PT           ##
## display only today schedule ##
#################################
def showPT(User,section_title):
	user = User
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	title = "View Pad and Partition"
	#create items for PT
	page = "PT"
	today = todayDate()
	pt = str(currentTimeProcess("PT"))
	item_plan = StatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start')
	items = list(item_plan)
	print str(items) +"show PT"
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_pt_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsM = list(item_planM)
	return render_to_response('PC/PT.html', locals())
#################################
##            for WH           ##
## display only today schedule ##
#################################
def showWH(User,section_title):
	user = User
	title = "View Warehouse"
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	page = "WH"
	today = todayDate()
	#create items for WH
	wh = currentTimeProcess("WH")
	item_plan = StatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start')
	items = list(item_plan)
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_wh_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsM = list(item_planM)
	return render_to_response('PC/WH.html',locals())
