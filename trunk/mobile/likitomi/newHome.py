from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import date
from app.models import Employee, FakeStatusTracking

#from likitomi import models.Employee,models.FakeStatusTracking

def allSection(request):
	eID = request.GET['eID']
	page =request.GET['page']
	today = todayDate()
	temp_contents = ''
	title = str(today)
	is_enable_table = True
	is_enable_desktop = True

	#section_title = employee.lastname
	employee = Employee.objects.get(eid=eID)
	section_title = "Homepage for " + page + " Login as " + employee.firstname + " " + employee.lastname
	if(page == "PC"):
		return showPC(eID,section_title)
	if(page == "MD"):
		return showMD(eID,section_title)
	if(page == "CR"):
		return showCR(eID,section_title)
	if(page == "CV"):
		return showCV(eID,section_title)
	if(page == "PT"):
		return showPT(eID,section_title)
	if(page == "WH"):
		return showWH(eID,section_title)
	
	return render_to_response('home.html', locals())
def todayDate():
	tempDate = date(2010,11,19)
	return tempDate
def showPC(eID,section_title):
	today = todayDate()
	#startList = 0
	#endList = 3
	#create items for PC
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id", "actual_wh_start", "actual_wh_end").order_by('plan_wh_start')
	items_plan_cr = list(item_plan_cr)
	items_plan_cv = list(item_plan_cv)
	items_plan_pt = list(item_plan_pt)
	items_plan_wh = list (item_plan_wh)
	
	cr = str(currentProcess("CR"))[2:8]
	cv = str(currentProcess("CV"))[2:8]
	cvThreeCS = str(currentProcess("3CS"))[2:8]
	cvThreeCL = str(currentProcess("3CL"))[2:8]
	cvTwoCL = str(currentProcess("2CL"))[2:8]
	pt = str(currentProcess("PT"))[2:8]
	wh = str(currentProcess("WH"))[2:8]
	#contents_text = len(items_plan_cr)
	pos = positionOfCurrentProcess("CR",cr)
	### limit view for 3 record and keep current task in the center ##
	## cr ##
	if pos > int(-1) and pos < 3:
		startList = 0
		endList = 3
	elif pos > int(len(items_plan_cr)-3) and pos < int(len(items_plan_cr)): 
		startList = len(items_plan_cr)-3
		endList = len(items_plan_cr)
	elif pos > 0:
		startList = pos-1
		endList = pos +1
	else:
		startList = 0
		endList = 0
	## cv ##
	pos = positionOfCurrentProcess("CV",cv)
	if pos > int(-1) and pos < 3:
		startList = 0
		endList = 3
	elif pos > int(len(items_plan_cv)-3) and pos < int(len(items_plan_cv)): 
		startList = len(items_plan_cv)-3
		endList = len(items_plan_cv)
	elif pos > 0:
		startList = pos-1
		endList = pos +1
	else:
		startList = 0
		endList = 0
	## pt ##
	#positionOfCurrentProcess(machine,product)
	pos = positionOfCurrentProcess("PT",pt)
	#contents_text = pos
	if pos > int(-1) and pos < 3:
		#contents_text = pos
		startList = 0
		endList = 3
	elif pos > int(len(items_plan_pt)-3) and pos < int(len(items_plan_pt)): 
		startList = len(items_plan_pt)-3
		endList = len(items_plan_pt)
	elif pos > 0:
		startList = pos-1
		endList = pos +1
	else:
		startList = 0
		endList = 0
	
	## wh ##
	pos = positionOfCurrentProcess("WH",wh)
	if pos > int(-1) and pos < 3:
		startList = 0
		endList = 3
	elif pos > int(len(items_plan_wh)-3) and pos < int(len(items_plan_wh)): 
		startList = len(items_plan_wh)-3
		endList = len(items_plan_wh)
	elif pos > 0:
		startList = pos-1
		endList = pos +1
	else:
		startList = 0
		endList = 0
	#contents_text = items_plan_cv
	items_plan_cr = items_plan_cr[startList:endList]
	items_plan_cv = items_plan_cv[startList:endList]
	items_plan_pt = items_plan_pt[startList:endList]
	items_plan_wh = items_plan_wh[startList:endList]
	#contents_text = items_plan_pt
	#contents_text = items_plan_pt
	#str(startList) +","+ str(endList)
	#contents_text = cvTwoCL
	return render_to_response('PC.html', locals())
def showMD(eID,section_title):
	return render_to_response('MD.html',locals())
def showCR(eID,section_title):
	today = todayDate()
	#create items for CR
	cr = str(currentProcess("CR"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	items = list(item_plan)
	return render_to_response('CR.html', locals())
def showCV(eID,section_title):
	today = todayDate()
	#create items for CV
	cvThreeCL = str(currentProcess("3CL"))[2:8]
	cvTwoCL = str(currentProcess("2CL"))[2:8]
	cvThreeCS = str(currentProcess("3CS"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('CV.html', locals())
def showPT(eID,section_title):
	#create items for PT
	today = todayDate()
	pt = str(currentProcess("PT"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('PT.html', locals())
def showWH(eID,section_title):
	today = todayDate()
	#create items for WH
	wh = str(currentProcess("WH"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_wh_start", "product_id").order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('WH.html',locals())
	
def positionOfCurrentProcess(machine,product):
	today = todayDate()
	position = 0
	#cr
	if(machine == "CR"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	#cv
	if(machine == "CV"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cr_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	if(machine == "3CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	if(machine == "3CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	if(machine == "2CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	#contents_text = machine
	if(machine == "PT"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("product_id")
			#contents_text = today_plan
			for pos, item in enumerate(today_plan):
				#contents_text = item
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	if(machine == "WH"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	return position
	
## get current process for each section ##
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
