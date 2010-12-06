from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
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
	startList = 0
	endList = 3
	employee = Employee.objects.get(eid=eID)
	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname
	if(employee.task == "PC"):
		item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')[startList:endList]
		item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')[startList:endList]
		item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')[startList:endList]
		item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id", "actual_wh_start", "actual_wh_end").order_by('plan_wh_start')[startList:endList]
		items_plan_cv = list(item_plan_cv)
		items_plan_pt = list(item_plan_pt)
		items_plan_wh = list (item_plan_wh)
	if(employee.task == "CR"):
		item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	if(employee.task == "CV"):
		item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	if(employee.task == "PT"):
		item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	if(employee.task == "WH"):
		item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id").order_by('plan_wh_start')
	page_section = employee.task
	items = list(item_plan)
	return render_to_response('home.html', locals())

def todayDate():
	tempDate = date(2010,11,19)
	return tempDate
