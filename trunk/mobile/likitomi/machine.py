from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import date
from app.models import Employee, FakeStatusTracking

def machine_list(request):
	today = todayDate()
	machine = request.GET['machine']
	eID = request.GET['eID']
	#create items for CV
	if(machine == "3CL"):
		cvThreeCL = str(currentProcess("3CL"))[2:8]
	if(machine == "2CL"):
		cvTwoCL = str(currentProcess("2CL"))[2:8]
	if(machine == "3CS"):
		cvThreeCS = str(currentProcess("3CS"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).filter(cv_machine=machine).values_list("plan_id","plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('machine.html', locals())

def todayDate():
	tempDate = date(2010,11,19)
	return tempDate
def currentProcess(machine):
	today=todayDate()
	if(machine=="CR"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("product_id","actual_cr_end")
			item_current = today_plan.filter(actual_cr_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	## top current for CV 
	if(machine=="CV"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	## current by machine
	if(machine == "3CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CS").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CL").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CL").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="PT"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("product_id","actual_pt_end")
			item_current = today_plan.filter(actual_pt_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="WH"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start').values_list("product_id","actual_wh_end")
			item_current = today_plan.filter(actual_wh_end = None).values_list("product_id")[0]
		except IndexError, error:
			item_current = 'idle'
	return item_current
