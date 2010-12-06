from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import date
from app.models import Employee, FakeStatusTracking

#from likitomi import models.Employee,models.FakeStatusTracking

def section(request):
	eID = request.GET['eID']
	today = todayDate()
	temp_contents = ''
	title = str(today)
	is_enable_table = True
	is_enable_desktop = True

	employee = Employee.objects.get(eid=eID)
	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname
	if(employee.task == "PC"):
		return showPC(section_title)
	if(employee.task == "CR"):
		return showCR(section_title)
	if(employee.task == "CV"):
		return showCV(section_title)
	if(employee.task == "PT"):
		return showPT(section_title)
	if(employee.task == "WH"):
		return showWH(section_title)
	
	return render_to_response('home.html', locals())

def todayDate():
	tempDate = date(2010,11,19)
	return tempDate
def showPC(section_title):
	today = todayDate()
	startList = 0
	endList = 3
	#create items for PC
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')[startList:endList]
	item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')[startList:endList]
	item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')[startList:endList]
	item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id", "actual_wh_start", "actual_wh_end").order_by('plan_wh_start')[startList:endList]
	items_plan_cr = list(item_plan_cr)
	items_plan_cv = list(item_plan_cv)
	items_plan_pt = list(item_plan_pt)
	items_plan_wh = list (item_plan_wh)
	return render_to_response('PC.html', locals())
def showCR(section_title):
	today = todayDate()
	#create items for CR
	item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	items = list(item_plan)
	return render_to_response('CR.html', locals())
def showCV(section_title):
	today = todayDate()
	#create items for CV
	#contents_text = currentProcess("CV")
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('CV.html', locals())
def showPT(section_title):
	#create items for PT
	today = todayDate()
	item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('PT.html', locals())
def showWH(section_title):
	today = todayDate()
	#create items for WH
	item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id").order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('WH.html',locals())
def currentProcess(machine):
	today=todayDate()
	if(machine=="CV"):
		today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("product_id","actual_cv_end")
		item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0]
	if(machine=="PT"):
		today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("product_id","actual_pt_end")
		item_current = today_plan.filter(actual_pt_end = None).values_list("product_id")[0]
	if(machine=="WH"):
		today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("product_id","actual_wh_end")
		item_current = today_plan.filter(actual_wh_end = None).values_list("product_id")[0]
	return item_current
