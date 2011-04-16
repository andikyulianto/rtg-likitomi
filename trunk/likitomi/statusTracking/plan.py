#Author: Chanaphan Prasomwong
# Last updated: 04/04/2010 
# Purpose: this file is containing function
# for the first time entering to the site 
# and check authentication of the page access 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from statusTracking.models import Employee, FakeStatusTracking
from statusTracking.utility import todayDate, currentProcess, currentTimeProcess, positionOfCurrentProcess, returnStartingPoint
from statusTracking.config import getPCItemNum
from datetime import date, datetime

########################
## display total Plan ##
########################

def totalPlan(request):
	title = "Total Plan"
	flashMessage =""
	eID = request.GET['eID']
	today = todayDate()
	page ="totalPlan"
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	return render_to_response('PC/plan.html', locals())

def totalPlanSelectedDate(request):
	title = "Total Plan"
	flashMessage =""
	today = todayDate()
#	eID = request.POST['eID']
#	datefrom =datetime.strptime(request.POST["from"], '%m/%d/%Y')
#	dateto =datetime.strptime(request.POST["to"], '%m/%d/%Y')
	datefrom = datetime(2011,03,12)
	dateto = datetime(2011,04,12)
	eID = "T101"
	today = todayDate()
	page ="totalPlanSelectedDate"
	items = FakeStatusTracking.objects.filter(plan_cr_start__range=(datefrom,dateto)).values_list("plan_id","product_id","cv_machine","plan_amount","plan_due").order_by('plan_due')
	return render_to_response('PC/totalPlan.html', locals())
