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
from django.db.models import Q, Sum
from statusTracking.utility import todayDate, currentTimeProcess, currentProcess
from statusTracking.models import AuthUser, StatusTracking, ProductCatalog, Products
from datetime import date, datetime
from employee import Employee
from statusTracking.config import getCVSpeed
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
	item_plan = StatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).filter(Q(cv_machine='3CS')|Q(cv_machine='2CL')|Q(cv_machine='4CD')|Q(cv_machine='3CM')|Q(cv_machine='3CL')).order_by('plan_cv_start')
	items = list(item_plan)
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_cv_start__range=(datefrominMonth,datetoinMonth)).filter(Q(cv_machine='3CS')|Q(cv_machine='2CL')|Q(cv_machine='4CD')|Q(cv_machine='3CM')|Q(cv_machine='3CL')).order_by('plan_due')
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
	item_plan = StatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).filter(Q(cv_machine='SS')|Q(cv_machine='RD')|Q(cv_machine='Remove')|Q(cv_machine='Foam')|Q(cv_machine='Tape')).order_by('plan_pt_start')
	items = list(item_plan)
#	print str(items) +"show PT"
	##monthlyPlan
	datefrominMonth = datetime(today.year,today.month,1)
	datetoinMonth = datetime(today.year,today.month,calendar.monthrange(today.year,today.month)[1])
	strThisMonth = today.strftime("%B")
	thisMonth = today.month
	item_planM = StatusTracking.objects.filter(plan_pt_start__range=(datefrominMonth,datetoinMonth)).filter(Q(cv_machine='SS')|Q(cv_machine='RD')|Q(cv_machine='Remove')|Q(cv_machine='Foam')|Q(cv_machine='Tape')).order_by('plan_due')
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
	item_planOut = StatusTracking.objects.filter(plan_due__year=today.year, plan_due__month=today.month, plan_due__day=today.day).order_by('plan_due')
	itemsOut = list(item_planOut)
	item_planM = StatusTracking.objects.filter(plan_wh_start__range=(datefrominMonth,datetoinMonth)).order_by('plan_due')
	itemsM = list(item_planM)
	return render_to_response('PC/WH.html',locals())

#####################################
## production and products details ##
#####################################
def showDetail(request):
	user = request.GET['user']
#	page =request.GET['page']
	mocode = request.GET['mocode']
	plan = StatusTracking.objects.get(plan_id = mocode )
	
	so = plan.sale_order_id
	po = plan.sale_order.purchase_order_no
	mo = plan.plan_id
	pcode = plan.product_id
	pname = plan.product.product_name
	customer =plan.product.partner.partner_name
	delivery = plan.plan_due
	due = plan.days_left
	
	
	plan_time_cr_in = plan.plan_cr_start
	plan_time_cr_out = plan.plan_cr_end
	plan_time_cv_in = plan.plan_cv_start
	plan_time_cv_out = plan.plan_cv_end
	plan_time_pt_in = plan.plan_pt_start
	plan_time_pt_out = plan.plan_pt_end
	plan_time_wh_in = plan.plan_wh_start
	plan_time_wh_out = plan.plan_due
	
	actual_time_cr_in = plan.actual_cr_start
	actual_time_cr_out = plan.actual_cr_end
	actual_time_cv_in = plan.actual_cv_start
	actual_time_cv_out = plan.actual_cv_end
	actual_time_pt_in = plan.actual_pt_start
	actual_time_pt_out = plan.actual_pt_end
	actual_time_wh_in = plan.actual_wh_start
	actual_time_wh_out = plan.actual_wh_end
	
	plan_amount = plan.plan_amount 
	actual_amount_cr_out = plan.actual_amount_cr * plan.product.cr_ratio_1 / plan.product.cr_ratio_2
	actual_amount_cv_in = plan.actual_amount_cv_in
	actual_amount_cv_out = plan.actual_amount_cv
	actual_amount_pt_in = plan.actual_amount_pt_in
	actual_amount_pt_out = plan.actual_amount_pt
	actual_amount_wh_in = plan.actual_amount_wh
	actual_amount_wh_out = plan.actual_amount_wh_out
	
	
	#CR
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = plan.product.partner.partner_name
	product = Products.objects.get(auto_id = plan.product_auto_id)
	flute = product.flute
	df = product.df
	bm = product.bm
	bl = product.bl
	cm = product.cm
	cl = product.cl
	width = product.width_mm
	length = product.length_mm
	case = plan.plan_amount
	cut = plan.cut
	blank = productCat.blank
	slit = productCat.slit
	scoreline = productCat.scoreline_d
	
	#CV
	color = productCat.rope_color
	req_2cl = productCat.req_2cl
	req_3cm = productCat.req_3cm
	req_3cs = productCat.req_3cs
	req_4cd = productCat.req_4cd
	req_3cl = productCat.req_3cl
	if(productCat.req_2cl ):
		machine = "2CL"
	elif(productCat.req_3cm):
		machine = "3CM"
	elif(productCat.req_3cs):
		machine = "3CS"
	elif(productCat.req_4cd):
		machine = "4CD"
	elif(productCat.req_3cl):
		machine = "3CL"
	else :
		machine =""
	time = plan.cv_time_used
	glue = productCat.req_gh
	hs = productCat.req_hs
	fg = productCat.req_fg
	cv_machine = productCat.next_process
	speed = getCVSpeed(cv_machine)
		
	#PT
	rd = productCat.req_rd
	ss = productCat.req_ss
	remove = productCat.req_remove
	foam = productCat.req_foam
	tape = productCat.req_tape

	page = "GM"
	return render_to_response('showDetail.html',locals())
#####################################
## production and products details ##
#####################################
def showStock(request):
	user = request.GET['user']
#	page =request.GET['page']
#	socode = request.GET['socode']
#	item_plan = StatusTracking.objects.filter(sale_order = socode)
#	items = list(item_plan)
	pcode = request.GET['pcode']
	
	plan = StatusTracking.objects.filter(product = pcode )
	items = list(plan)
	sum_plan = StatusTracking.objects.filter(product = pcode ).aggregate(plan_amount=Sum('plan_amount'),actual_amount_wh_in=Sum('actual_amount_wh'),actual_amount_wh_out=Sum('actual_amount_wh_out'))
	items_sum = list(sum_plan)
#	pcode = plan.product_id
#	pname = plan.product.product_name
#	customer =plan.product.partner.partner_name
#	delivery = plan.plan_due
#	due = plan.days_left
	return render_to_response('stockDetail.html',locals())
