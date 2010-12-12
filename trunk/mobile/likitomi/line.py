from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import date
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
	task = "CR"
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
	amount = plan.plan_amount
	task = "CR"
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
	task = "CV"
	return render_to_response('updateStartCV.html',locals())
def endPT(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = plan.plan_amount
	task = "CV"
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
	task = "CV"
	return render_to_response('updateStartCV.html',locals())
def endCV(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = plan.plan_amount
	task = "CV"
	return render_to_response('updateEndCV.html',locals())
def startWH(request):
	return render_to_response('updateStartWH.html',locals())
def endWH(request):
	content_header = "Finish"
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	plan = FakeStatusTracking.objects.get(plan_id = planID)
	amount = plan.plan_amount
	task = "WH"
	return render_to_response('updateEndWH.html',locals())
def todayDate():
	tempDate = date(2010,11,19)
	return tempDate

