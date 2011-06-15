# Author: Chanaphan Prasomwong
# Last updated: 26/03/2010 
# Purpose: this file is containing function
# for displaying homepage for each person
# After logging in by using user ID 
# This page will check the department and
# return the personalised homepage for each person

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from statusTracking.models import StatusTracking, ProductCatalog, Partners
from statusTracking.utility import todayDate, currentProcess, currentTimeProcess, positionOfCurrentProcess, returnStartingPoint
from statusTracking.config import getPCItemNum
from datetime import date, datetime
from django.db.models import F
from django.utils.safestring import mark_safe
import calendar
from employee import Employee
#import loggingex


user = ""
def set_username(user):
	global username
	username = user
	return username

####################################################
##                    for pc                      ##
## this page is view process via desktop computer ##
####################################################
def section(request):
#	FORMAT = "%(asctime)-15s %(clientip)s %(user)-8s %(message)s"
#	logging.basicConfig(format=FORMAT)
#	d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
#	logging.warning("Protocol problem: %s", "connection reset", extra=d)
	try:
		eID = request.GET['eID']
		employee = AuthUser.objects.get(eid=eID)
	except:
		user = request.GET['user']
		employee = Employee(user)
		username = employee.username
		set_username(user)
		eID = employee.id
#		task = employee.task
	today = todayDate()
	
	
	task = employee.task
#	print "this is task " +str(task)

	page =  str(task)

	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname

	if(page == "PC"):
		return showPC(user,section_title)
	elif(page == "GM"):
		return showGM(user,section_title)
	elif(page == "CR"):
		return workCR(user,section_title)
	elif(page == "CV"):
		return workCV(user,section_title)
	elif(page == "PT"):
		return workPT(user,section_title)
	elif(page == "WH"):
		return workWH(user,section_title)
	else :
		return render_to_response('home.html', locals())
	print "return home.html"
	return render_to_response('home.html', locals())

def showPC(user,title):
	#print "enter showPC"
#	logging.error("enter showPC")
	today = todayDate()
	page = "PC"
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	username = user
	
	#create items for PC
	#extra = db_type(StatusTracking.objects.all())
	#item_plan_cr = StatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_code","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	#temp_contents = extra[0].days_left
	item_plan_cr = StatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start')
	item_plan_cv = StatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start')
	item_plan_pt = StatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start')
	item_plan_wh = StatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start')
	print StatusTracking
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



############################################

##########################
	########Monthly###########
	##########################
	today = todayDate()
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	#page ="totalPlanSelectedDate"
	#temp_contents = StatusTracking.objects.all()

#	items= StatusTracking.objects.all() #filter(plan_cr_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	query = StatusTracking.objects.values_list('plan_cr_start')

	qlist = list(query)
	items = list()
	for lst in qlist:
		nlst = list(lst)
		items.append(nlst)

	print "return PC/view.html"
	return render_to_response('PC/view.html', locals())



def normalPlanRefresher(request):
	print "enter normalPlanRefresher"
	today = todayDate()
	page = "PC"
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	username = user
	
	#create items for PC
	#extra = db_type(StatusTracking.objects.all())
	#item_plan_cr = StatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_code","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	#temp_contents = extra[0].days_left
	item_plan_cr = StatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start')
	item_plan_cv = StatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start')
	item_plan_pt = StatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start')
	item_plan_wh = StatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start')
	print StatusTracking
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
	print "return PC/PC.html"
	return render_to_response('PC/PC.html', locals())

def lastUpdate(request):
###########################################
############# not in process ##############
###########################################
	print "enter lastUpdate"
	today = todayDate()
	print "PC/lastUpdate.html"
	return render_to_response('PC/lastUpdate.html',locals())

def monthlyPlan(request):
	##########################
	########Monthly###########
	##########################
	today = todayDate()
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	eID = "T101"
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	page ="totalPlanSelectedDate"
	#temp_contents = StatusTracking.objects.all()

	items = StatusTracking.objects.filter(plan_cr_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsNotProcess = StatusTracking.objects.filter(plan_cr_start__range=(datefrominMonth,datetoinMonth)).exclude(actual_wh_start__isnull=False).order_by('plan_due')
	itemsMissing = StatusTracking.objects.filter(plan_cr_start__range=(datefrominMonth,datetoinMonth)).exclude(actual_amount_wh__gte=F('plan_amount')).exclude(actual_wh_start__isnull=True).order_by('plan_due')
	print "PC/monthlyPlan.html"
	return render_to_response('PC/monthlyPlan.html',locals())

###################################################
##                 for manager                   ##
## this page is view process via mobile computer ##
###################################################
#Note : not complete
def showGM(eID,title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today= todayDate()
	showGM_items = StatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("product_id","plan_amount","actual_amount_cr","plan_cr_start","actual_amount_cv","plan_cv_start","actual_amount_pt","plan_pt_start","actual_amount_wh","plan_wh_start","plan_due")
	content_header = "Please select product item in order to view realtime progress"
	return render_to_response('GM/GM.html',locals())

#####################################	
##             for CR              ##
## time and process are recordable ##
#####################################
def workCR(user,title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	username = user
	today = todayDate()
	employee = Employee(user)
	eID = employee.id
	page = "CR"
	today = todayDate()
	#create items for CR
	if(currentProcess("CR")=='idle'):
		cr = 'idle'
	else:
		cr = str(currentProcess("CR"))
	#temp_contents = cr
	item_plan = StatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start')
	items = list(item_plan)
	x = ''
	return render_to_response('CR/listCR.html', locals())
#	return render_to_response('content_cr.html',locals())	
#####################################	
##             for CV              ##
## time and process are recordable ##
#####################################
def workCV(user,title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	username = user
	page = "CV"
	today = todayDate()
	employee = Employee(user)
	eID = employee.id
	cv = currentTimeProcess("CV")

	#create items for CV
	if(currentProcess("3CS")=='idle'):
		cvThreeCS = 'idle'
	else:
		cvThreeCS = str(currentProcess("3CS"))[3:9]
	if(currentProcess("3CL")=='idle'):
		cvThreeCL = 'idle'
	else:
		cvThreeCL = str(currentProcess("3CL"))[3:9]
	if(currentProcess("2CL")=='idle'):
		cvTwoCL = 'idle'
	else:
		cvTwoCL = str(currentProcess("2CL"))[3:9]
	if(currentProcess("3CW")=='idle'):
		cvThreeCW = 'idle'
	else:
		cvThreeCW = str(currentProcess("3CW"))[3:9]
	if(currentProcess("2CS")=='idle'):
		cvTwoCS = 'idle'
	else:
		cvTwoCS = str(currentProcess("2CS"))[3:9]
	cvThreeCS = currentTimeProcess("3CS")
	cvThreeCL = currentTimeProcess("3CL")
	cvTwoCL = currentTimeProcess("2CL")
	cvThreeCW = currentTimeProcess("3CW")
	cvTwoCS = currentTimeProcess("2CS")
	item_plan = StatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('CV/listCV.html', locals())

#####################################	
##             for PT              ##
## time and process are recordable ##
#####################################
def workPT(user,title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	username = user
	page= "PT"
	today = todayDate()
	employee = Employee(user)
	eID = employee.id
	#create items for PT
	today = todayDate()
	pt = str(currentTimeProcess("PT"))
	item_plan = StatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('PT/listPT.html', locals())

#####################################	
##             for WH              ##
## time and process are recordable ##
#####################################

def workWH(user,title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	global username
	page = "WH"
	username = user
	today = todayDate()
	employee = Employee(user)
	eID = employee.id
	today = todayDate()
	#create items for WH
	wh = currentTimeProcess("WH")
	item_plan = StatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('WH/listWH.html',locals())
	

##############################
## Display the detail pages ##
##############################
def display(request):
	productID= request.GET['product']
	plan_amount = StatusTracking.objects.filter(product=productID).values_list("plan_amount")[0][0]
	so = ''
	po = StatusTracking.objects.filter(product=productID).values_list("plan_id")[0][0]
	#product_name = "product_name"
	product_name = ProductCatalog.objects.filter(product_code = productID).values_list("product_name")[0][0]
	partner_code = ProductCatalog.objects.filter(product_code = productID).values_list("partner_id")[0][0]
	partner = Partners.objects.filter(partner_id = partner_code).values_list("partner_name")[0][0]
	return render_to_response('PC/productDetail.html',locals())

