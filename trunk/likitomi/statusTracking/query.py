from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import F
from statusTracking.models import Employee, FakeStatusTracking
from statusTracking.utility import todayDate
from datetime import date, datetime,timedelta
def queryDateNotProcess(request):
#	eID = request.GET['eID']
#	datefrom = request.GET['from']
#	dateto = request.GET['to']
	eID="T101"
	datefrom = datetime(2011, 03, 12)
	dateto = datetime(2011,04,12)
	today = todayDate()
	title = str(today)
	employee = Employee.objects.get(eid=eID)
	page =  employee.task

	
	notProcessCR = FakeStatusTracking.objects.filter(plan_cr_start__range=(datefrom,dateto)).exclude(actual_cr_end__isnull=False).exclude(plan_cr_end__isnull=True).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	notProcessCV = FakeStatusTracking.objects.filter(plan_cv_start__range=(datefrom,dateto)).exclude(actual_cv_end__isnull=False).exclude(plan_cv_end__isnull=True).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine","process1","plan_due","plan_amount","actual_amount_cv").order_by('plan_cv_start')
	notProcessPT = FakeStatusTracking.objects.filter(plan_pt_start__range=(datefrom,dateto)).exclude(actual_pt_end__isnull=False).exclude(plan_pt_end__isnull=True).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end","process2","plan_due","plan_amount","actual_amount_cv").order_by('plan_pt_start')
	notProcessWH = FakeStatusTracking.objects.filter(plan_wh_start__range=(datefrom,dateto)).exclude(actual_wh_start__isnull=False).exclude(plan_wh_start__isnull=True).values_list("plan_wh_start", "product_id","actual_wh_start","process1","process2","process3","plan_due","plan_amount","actual_amount_wh").order_by('plan_wh_start')
	return render_to_response('PC/notInProcess.html', locals())
def queryDateMissing(request):
#	eID = request.GET['eID']
#	datefrom = request.GET['from']
#	dateto = request.GET['to']
	eID="T101"
	datefrom = datetime(2011, 03, 12)
	dateto = datetime(2011,04,12)
	today = todayDate()
	title = str(today)
	employee = Employee.objects.get(eid=eID)
	page =  employee.task

	
	missingInCR = FakeStatusTracking.objects.filter(plan_cr_start__range=(datefrom,dateto)).exclude(actual_amount_cr__gte= F('plan_amount')).exclude(actual_cr_end__isnull=True).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	missingInCV = FakeStatusTracking.objects.filter(plan_cv_start__range=(datefrom,dateto)).exclude(actual_amount_cv__gte= F('plan_amount')).exclude(actual_cv_end__isnull=True).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine","process1","plan_due","plan_amount","actual_amount_cv").order_by('plan_cv_start')
	missingInPT = FakeStatusTracking.objects.filter(plan_pt_start__range=(datefrom,dateto)).exclude(actual_amount_pt__gte=F('plan_amount')).exclude(actual_pt_end__isnull=True).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end","process2","plan_due","plan_amount","actual_amount_pt").order_by('plan_pt_start')
	missingInWH = FakeStatusTracking.objects.filter(plan_wh_start__range=(datefrom,dateto)).exclude(actual_amount_wh__gte=F('plan_amount')).exclude(actual_wh_start__isnull=True).values_list("plan_wh_start", "product_id","actual_wh_start","process1","process2","process3","plan_due","plan_amount","actual_amount_wh").order_by('plan_wh_start')
	return render_to_response('PC/missing.html', locals())
