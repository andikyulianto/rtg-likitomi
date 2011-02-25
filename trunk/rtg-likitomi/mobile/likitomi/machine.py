# Author: Chanaphan Prasomwong
# Last updated: 11/1/2010 
# Purpose: this file is containing function
# for displaying homepage for each person
# After logging in by using user ID 
# This page will check the department and
# return the personalised homepage for each person

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from utility import todayDate, currentProcess
from app.models import Employee, FakeStatusTracking

###############################################################
## this page is will filter for only a particular CV machine ##
###############################################################
def machine_list(request):
	today = todayDate()
	machine = request.GET['machine']
	eID = request.GET['eID']
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	#create items for CV
	if(machine == "3CL"):
		cvThreeCL = str(currentProcess("3CL"))[2:8]
	if(machine == "2CL"):
		cvTwoCL = str(currentProcess("2CL"))[2:8]
	if(machine == "3CS"):
		cvThreeCS = str(currentProcess("3CS"))[2:8]
	if(machine == "2CS"):
		cvTwoCS = str(currentProcess("2CS"))[2:8]
	if(machine == "3CW"):
		cvThreeCW = str(currentProcess("3CW"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).filter(cv_machine=machine).values_list("plan_id","plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('machine.html', locals())


