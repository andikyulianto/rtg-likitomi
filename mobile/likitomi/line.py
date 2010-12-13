from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import datetime
from app.models import Employee, FakeStatusTracking, ProductCatalog, Products

def startCR(request):
	content_header = "Load"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
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
	return render_to_response('updateStartCR.html', locals())
def endCR(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID )
	amount = str(plan.plan_amount)
	task = "end"
	at = "CR"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('updateEndCR.html',locals())
def startCV(request):
	content_header = "Load"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID
	current_date_time = todayDate()
	task = "start"
	at = "CV"
	return render_to_response('updateStartCV.html',locals())
def endCV(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "CV"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('updateEndCV.html',locals())
def startPT(request):
	content_header = "Load"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	product_code = plan.product_id
	productCat = ProductCatalog.objects.get(product_code = product_code)
	product_name = productCat.product_name
	cname = productCat.cname
	product = Products.objects.get(product_code = product_code)
	amount = plan.plan_amount
	pID = planID
	current_date_time = todayDate()
	task = "start"
	at = "PT"
	return render_to_response('updateStartCV.html',locals())
def endPT(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "PT"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('updateEndCV.html',locals())
def startWH(request):
	content_header = "In"
	eID = request.GET['eID']
	planID = request.GET['pID']
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	today = todayDate()
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
	return render_to_response('updateStartWH.html',locals())
def endWH(request):
	content_header = "Out"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = str(plan.plan_amount)
	task = "end"
	at = "WH"
	current_date_time = todayDate()
	pID = planID
	return render_to_response('updateEndWH.html',locals())
def todayDate():
	tempDate = datetime.now()
	return tempDate.strftime("%Y-%m-%d %H:%M:%S")

