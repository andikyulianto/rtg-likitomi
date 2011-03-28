# Author: Chanaphan Prasomwong
# Last updated: 11/1/2010 
# Purpose: this file is containing function
# for recording start and stop time in each section 
# that will be used by workers in the production lines
#

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from statusTracking.utility import todayDate
from statusTracking.config import getCVSpeed
from statusTracking.models import Employee, FakeStatusTracking, ProductCatalog, Products

###########################################
##                 for CR                ##
## to gatter information before stamping ##
##    of the loaded time of corrugator   ##
###########################################

def startCR(request):
	content_header = "Load"
	
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	#plan = Employee.objects.get(eid=eID)
	plan = FakeStatusTracking.objects.get(plan_id = planID )
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = productCat.cname
	product = Products.objects.get(product_code = product_code)
	flute = product.flute
	df = product.df
	bm = product.bm
	bl = product.bl
	cm = product.cm
	cl = product.cl
	width_mm = product.width_mm
	length_mm = product.length_mm
	cut = productCat.cut
	blank = productCat.blank
	slit = productCat.slit
	scoreline = productCat.scoreline_d
	next_process = productCat.next_process
	amount = plan.plan_amount
	task = "start"
	at = "CR"
	current_date_time = todayDate()
	pID = planID
	#product = ProductCatalog.objects.filter(product_code= product_id)
	#product_name = product.product_name
	#product = list(ProductCatalog.objects.all())
	title = "starting "+product_code+" in corrugator"
	return render_to_response('CR/updateStartCR.html', locals())

###########################################
##                 for CR                ##
## to gatter information before stamping ##
##   of the finished time of corrugator  ##
###########################################

def endCR(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
###
	plan = FakeStatusTracking.objects.get(plan_id = planID )
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = productCat.cname
	product = Products.objects.get(product_code = product_code)
	flute = product.flute
	df = product.df
	bm = product.bm
	bl = product.bl
	cm = product.cm
	cl = product.cl
	width_mm = product.width_mm
	length_mm = product.length_mm
	cut = productCat.cut
	blank = productCat.blank
	slit = productCat.slit
	scoreline = productCat.scoreline_d
	next_process = productCat.next_process
	amount = plan.plan_amount
	task = "start"
	at = "CR"
	current_date_time = todayDate()
	pID = planID
	#product = ProductCatalog.objects.filter(product_code= product_id)
	#product_name = product.product_name
	#product = list(ProductCatalog.objects.all())
	title = "Finished "+product_code+" in corrugator"
###
	task = "end"
	at = "CR"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('CR/updateEndCR.html',locals())

###########################################
##                 for CV                ##
## to gatter information before stamping ##
##    of the loaded time of corrugator   ##
###########################################
def startCV(request):
	content_header = "Load"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)

	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	color = productCat.rope_color
	cv_machine = productCat.next_process
	speed = getCVSpeed(cv_machine)
	product_name = productCat.product_name
	partner = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID
	current_date_time = todayDate()
	task = "start"
	at = "CV"
	title = "starting "+product_code+" in convertor"
	return render_to_response('CV/updateStartCV.html',locals())

###########################################
##                 for CV                ##
## to gatter information before stamping ##
##   of the finished time of corrugator  ##
###########################################
def endCV(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "CV"
	current_date_time = todayDate()
	##
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	color = productCat.rope_color
	cv_machine = productCat.next_process
	speed = getCVSpeed(cv_machine)
	product_name = productCat.product_name
	partner = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID
	##	
	title = "Finished "+product_code+" in corvertor"
	return render_to_response('CV/updateEndCV.html',locals())
	
###########################################
##                 for PT                ##
## to gatter information before stamping ##
##    of the loaded time of corrugator   ##
###########################################
def startPT(request):
	content_header = "Load"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)

	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	color = productCat.rope_color
	cv_machine = productCat.next_process
	speed = getCVSpeed(cv_machine)
	product_name = productCat.product_name
	partner = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID
	current_date_time = todayDate()
	task = "start"
	at = "PT"
	title = "Starting "+product_code+" in pad /partition"
	return render_to_response('PT/updateStartCV.html',locals())

###########################################
##                 for PT                ##
## to gatter information before stamping ##
##   of the finished time of corrugator  ##
###########################################
def endPT(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "PT"
	current_date_time = todayDate()


	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	color = productCat.rope_color
	cv_machine = productCat.next_process
	speed = getCVSpeed(cv_machine)
	product_name = productCat.product_name
	partner = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID

	title = "Finished "+product_code+" in pad /partition"
	return render_to_response('PT/updateEndCV.html',locals())
	
###########################################
##                 for WH                ##
## to gatter information before stamping ##
##    of the loaded time of corrugator   ##
###########################################
def startWH(request):
	content_header = "In"
	eID = request.GET['eID']
	planID = request.GET['pID']
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = str(plan.plan_amount)
	pID = planID
	current_date_time = todayDate()
	task = "start"
	at = "WH"
	title = "Finished "+product_code+" warehouse"
	return render_to_response('WH/updateStartWH.html',locals())

###########################################
##                 for WH                ##
## to gatter information before stamping ##
##   of the finished time of corrugator  ##
###########################################
def endWH(request):
	content_header = "Out"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "WH"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('updateEndWH.html',locals())

