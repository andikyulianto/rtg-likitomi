from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from app.models import Employee, FakeStatusTracking
from utility import todayDate, currentProcess, positionOfCurrentProcess

# use PC.html template
def section(request):
	eID = request.GET['eID']
	today = todayDate()
	temp_contents = ''
	title = str(today)
	is_enable_table = True
	is_enable_desktop = True

	employee = Employee.objects.get(eid=eID)
	page =  employee.task
	#section_title = employee.lastname
	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname
	if(page == "PC"):
		return showPC(eID,section_title)
	if(page == "MD"):
		return showMD(eID,section_title)
	if(page == "CR"):
		return workCR(eID,section_title)
	if(page == "CV"):
		return workCV(eID,section_title)
	if(page == "PT"):
		return workPT(eID,section_title)
	if(page == "WH"):
		return workWH(eID,section_title)
	
	return render_to_response('home.html', locals())

def showPC(eID,section_title):
	today = todayDate()
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	#startList = 0
	#endList = 3
	#create items for PC
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_wh_start", "product_id", "actual_wh_start").order_by('plan_wh_start')
	items_plan_cr = list(item_plan_cr)
	items_plan_cv = list(item_plan_cv)
	items_plan_pt = list(item_plan_pt)
	items_plan_wh = list (item_plan_wh)
	
	cr = str(currentProcess("CR"))[2:8]
	cv = str(currentProcess("CV"))[2:8]
	cvThreeCS = str(currentProcess("3CS"))[2:8]
	cvThreeCL = str(currentProcess("3CL"))[2:8]
	cvTwoCL = str(currentProcess("2CL"))[2:8]
	cvThreeCW = str(currentProcess("3CW"))[2:8]
	cvTwoCS = str(currentProcess("2CS"))[2:8]
	pt = str(currentProcess("PT"))[2:8]
	wh = str(currentProcess("WH"))[2:8]
	
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
	wh = positionOfCurrentProcess("WH",wh)
	if pos < 3:
		startListWH = 0
		endListWH = 3
	elif pos > int(len(items_plan_wh)-3) and pos < int(len(items_plan_wh)): 
		startListWH = len(items_plan_wh)-3
		endListWH = len(items_plan_wh)
	elif pos > 0:
		startListWH = pos-1
		endListWH = pos +1
	else:
		startListWH = 0
		endListWH = 0
	#contents_text = items_plan_cv
	items_plan_cr = items_plan_cr[startList:endList]
	items_plan_cv = items_plan_cv[startList:endList]
	items_plan_pt = items_plan_pt[startList:endList]
	#items_plan_wh = items_plan_wh[startListWH:endListWH]
	#contents_text = items_plan_pt
	#contents_text = items_plan_pt
	#str(startList) +","+ str(endList)
	#contents_text = cvTwoCL
	return render_to_response('PC.html', locals())
def showMD(eID,section_title):
	return render_to_response('MD.html',locals())
def workCR(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	eID = eID
	today = todayDate()
	#create items for CR
	cr = str(currentProcess("CR"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_id","plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')
	items = list(item_plan)
	return render_to_response('listCR.html', locals())
def workCV(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today = todayDate()
	#create items for CV
	cvThreeCS = str(currentProcess("3CS"))[2:8]
	cvThreeCL = str(currentProcess("3CL"))[2:8]
	cvTwoCL = str(currentProcess("2CL"))[2:8]
	cvThreeCW = str(currentProcess("3CW"))[2:8]
	cvTwoCS = str(currentProcess("2CS"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).values_list("plan_id","plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')
	items = list(item_plan)
	return render_to_response('listCV.html', locals())
def workPT(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	#create items for PT
	today = todayDate()
	pt = str(currentProcess("PT"))[2:8]
	item_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).values_list("plan_id","plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')
	items = list(item_plan)
	return render_to_response('listPT.html', locals())
def workWH(eID,section_title):
	is_enable_leftbutton = True
	is_enable_rightbutton = True
	today = todayDate()
	#create items for WH
	wh = str(currentProcess("WH"))[2:8]
	#wh = currentTimeProcess("WH")
	item_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_id","plan_wh_start", "product_id","actual_wh_start").order_by('plan_wh_start')
	items = list(item_plan)
	return render_to_response('listWH.html',locals())
	
#def positionOfCurrentProcess(machine,product):
#	today = todayDate()
#	position = 0
#	#cr
#	if(machine == "CR"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	#cv
#	if(machine == "CV"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cr_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "3CL"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "3CS"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "2CL"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "3CW"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "2CS"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	#contents_text = machine
#	if(machine == "PT"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("product_id")
#			#contents_text = today_plan
#			for pos, item in enumerate(today_plan):
#				#contents_text = item
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	if(machine == "WH"):
#		try:
#			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).order_by('plan_wh_start').values_list("product_id")
#			for pos, item in enumerate(today_plan):
#				if str(item)[2:8] == product:
#					position = pos
#		except IndexError, error:
#			position = -1
#	return position

def currentTimeProcess(machine):
	today=todayDate()
	if(machine=="CR"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("product_id","actual_cr_end")
			item_current = today_plan.filter(actual_cr_end = None).values_list("plan_cr_start")[0]
		except IndexError, error:
			item_current = 'idle'
	## top current for CV 
	if(machine=="CV"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	## current by machine
	if(machine == "3CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CS").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CL").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CL").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CW"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CW").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CS").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("plan_cv_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="PT"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("product_id","actual_pt_end")
			item_current = today_plan.filter(actual_pt_end = None).values_list("plan_pt_start")[0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="WH"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("product_id","actual_wh_start").order_by('plan_wh_start')
			item_current = today_plan.filter(actual_wh_start = None).values_list("plan_wh_start")[0]
			item_current = item_current[0]
			#item_current = item_current.strftime("%H:%M")
		except IndexError, error:
			item_current = 'idle'
	return item_current

##############################
## Display the detail pages ##
##############################
def display(request):
	product= request.GET['product']
	plan_amount = FakeStatusTracking.objects.filter(product_id=product).values_list("plan_amount")
	return render_to_response('productDetail.html',locals())

