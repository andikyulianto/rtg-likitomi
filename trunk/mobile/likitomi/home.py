# Author: Chanaphan Prasomwong
# Last updated: 11/1/2010 
# Purpose: this file is containing function
# for displaying homepage for each person
# After logging in by using user ID 
# This page will check the department and
# return the personalised homepage for each person

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from app.models import Employee, FakeStatusTracking, ProductCatalog, Partners
from utility import todayDate, currentProcess, currentTimeProcess, positionOfCurrentProcess, returnStartingPoint
from config import getPCItemNum

####################################################
##                    for pc                      ##
## this page is view process via desktop computer ##
####################################################
def section(request):
	eID = request.GET['eID']
	today = todayDate()
	temp_contents = ''

	title = str(today)
	is_enable_table = True
	is_enable_desktop = True

	employee = Employee.objects.get(eid=eID)
	page =  employee.task
	#section_title = employee.lastname
	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname
	if(page == "PC"):
		return showPC(eID,section_title)
	if(page == "GM"):
		return showMD(eID,section_title)
	if(page == "CR"):
		return workCR(eID,section_title)
	if(page == "CV"):
		return workCV(eID,section_title)
	if(page == "PT"):
		return workPT(eID,section_title)
	if(page == "WH"):
		return workWH(eID,section_title)
	
	return render_to_response('home.html', locals())

def showPC(eID,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True

	#create items for PC
	#extra = db_type(FakeStatusTracking.objects.all())
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end","days_left").order_by('plan_cr_start')
	#temp_contents = extra[0].days_left
	#item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end").order_by('plan_cr_start')
	#item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year=
	item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine","process1","plan_due").order_by('plan_cv_start')
	item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end","process2","plan_due").order_by('plan_pt_start')
	#bug here ordering (also in utility line67)
	item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_wh_start", "product_id","actual_wh_start","process1","process2","process3","plan_due").order_by('plan_wh_start')
	
	items_plan_cr = list(item_plan_cr)
	items_plan_cv = list(item_plan_cv)
	items_plan_pt = list(item_plan_pt)
	items_plan_wh = list (item_plan_wh)
	
	cr = currentTimeProcess("CR")
	cv = currentTimeProcess("CV")
	cvThreeCS = currentTimeProcess("3CS")
	cvThreeCL = currentTimeProcess("3CL")
	cvTwoCL = currentTimeProcess("2CL")
	cvThreeCW = currentTimeProcess("3CW")
	cvTwoCS = currentTimeProcess("2CS")
	pt = currentTimeProcess("PT")
	wh = currentTimeProcess("WH")
	currentTimeProcess("WH") 
	
	#prepare list for CR
	size = len(items_plan_cr)
	if(currentProcess("CR")!='idle'):
		pos = positionOfCurrentProcess("CR",currentProcess("CR")[0][0:8])
	else :
		pos = size
	#temp_contents = currentProcess("CV")
	startList = returnStartingPoint(pos,size)
	endList = startList+getPCItemNum()
	items_plan_cr=items_plan_cr[startList:endList]
	
	#prepare list for CV
	size = len(items_plan_cv)
	pos = positionOfCurrentProcess("CV",currentProcess("CV")[0][0:8])
	startList = returnStartingPoint(pos,size)
	endList = startList+getPCItemNum()
	items_plan_cv=items_plan_cv[startList:endList]
	
	#prepare list for PT
	size = len(items_plan_pt)
	pos = positionOfCurrentProcess("PT",currentProcess("PT")[0][0:8])
	startList = returnStartingPoint(pos,size)
	endList = startList+getPCItemNum()
	items_plan_pt=items_plan_pt[startList:endList]
	
	#prepare list for WH
	size = len(items_plan_wh)
	#pos =currentProcess("WH")[0][0]
	#temp_contents = currentProcess("WH")[0][0]
	pos = positionOfCurrentProcess("WH",currentProcess("WH")[0][0])
	startList = returnStartingPoint(pos,size)
	endList = startList+getPCItemNum()
	items_plan_wh=items_plan_wh[startList:endList]
	#temp_contents = currentProcess("2CL")
	return render_to_response('PC.html', locals())
	
###################################################
##                 for manager                   ##
## this page is view process via mobile computer ##
###################################################
#Note : not complete
def showMD(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today= todayDate()
	showMD_items = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("product_id","plan_amount","actual_amount_cr","plan_cr_start","actual_amount_cv","plan_cv_start","actual_amount_pt","plan_pt_start","actual_amount_wh","plan_wh_start","plan_due")
	content_header = "Please select product item in order to view realtime progress"
	return render_to_response('MD.html',locals())

#####################################	
##             for CR              ##
## time and process are recordable ##
#####################################
def workCR(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	eID = eID
	today = todayDate()
	#create items for CR
	if(currentProcess("CR")=='idle'):
		cr = 'idle'
	else:
		cr = str(currentProcess("CR"))[2:8]
	#temp_contents = cr
	item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_id","plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	items = list(item_plan)
	x = ''
	return render_to_response('listCR.html', locals())
#	return render_to_response('content_cr.html',locals())	
#####################################	
##             for CV              ##
## time and process are recordable ##
#####################################
def workCV(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today = todayDate()
	#create items for CV
	if(currentProcess("3CS")=='idle'):
		cvThreeCS = 'idle'
	else:
		cvThreeCS = str(currentProcess("3CS"))[2:8]
	if(currentProcess("3CL")=='idle'):
		cvThreeCL = 'idle'
	else:
		cvThreeCL = str(currentProcess("3CL"))[2:8]
	if(currentProcess("2CL")=='idle'):
		cvTwoCL = 'idle'
	else:
		cvTwoCL = str(currentProcess("2CL"))[2:8]
	if(currentProcess("3CW")=='idle'):
		cvThreeCW = 'idle'
	else:
		cvThreeCW = str(currentProcess("3CW"))[2:8]
	if(currentProcess("2CS")=='idle'):
		cvTwoCS = 'idle'
	else:
		cvTwoCS = str(currentProcess("2CS"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_id","plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "process1","process3","process4").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('listCV.html', locals())

#####################################	
##             for PT              ##
## time and process are recordable ##
#####################################
def workPT(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	#create items for PT
	today = todayDate()
	pt = str(currentTimeProcess("PT"))
	item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_id","plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end","process2","process4").order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('listPT.html', locals())

#####################################	
##             for WH              ##
## time and process are recordable ##
#####################################

def workWH(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today = todayDate()
	#create items for WH
	wh = currentTimeProcess("WH")
	item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_id","plan_wh_start", "product_id","actual_wh_start","process1","process2","process3").order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('listWH.html',locals())
	

##############################
## Display the detail pages ##
##############################
def display(request):
	product= request.GET['product']
	plan_amount = FakeStatusTracking.objects.filter(product_id=product).values_list("plan_amount")[0][0]
	so = ''
	po = FakeStatusTracking.objects.filter(product_id=product).values_list("plan_id")[0][0]
	#product_name = "product_name"
	product_name = ProductCatalog.objects.filter(product_code = product).values_list("product_name")[0][0]
	partner_code = ProductCatalog.objects.filter(product_code = product).values_list("partner_id")[0][0]
#	partner = Partners.objects.filter(partner_id = partner_code).values_list("partner_name")[0][0]
	return render_to_response('productDetail.html',locals())

