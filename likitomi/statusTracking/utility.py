from datetime import date, datetime
from statusTracking.models import Employee, FakeStatusTracking
from statusTracking.config import getPCItemNum

##########################################
## get current process for each section ##
##        return product code           ##
##########################################
def todayDate():
	tempDate = datetime.now()
	#tempDate = date(2011,02,18)
	#strftime("%Y-%m-%d %H:%M:%S"))
	return tempDate
def returnall():
	return list(FakeStatusTracking.objects.all())

##########################################
## get current process for each section ##
##        return product code           ##
##########################################
def currentProcess(machine):
	today=todayDate()
	print today
	if(machine=="CR"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("product_id")
			#item_current = list(today_plan)
			item_current = list(today_plan.filter(actual_cr_end = None).values_list("product_id"))[0][0]
		except IndexError, error:
			item_current = 'idle'
	## top current for CV 
	if(machine=="CV"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
			item_current = list(today_plan.filter(actual_cv_end = None).values_list("product_id"))[0][0]
		except IndexError, error:
			item_current = 'idle'
	## current by machine
	if(machine == "3CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CS").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CL").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CL").values_list("product_id","actual_cv_end")
			#item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id", "actual_cr_end")
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CW"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CW").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CS").values_list("product_id","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="PT"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("product_id","actual_pt_end")
			item_current = today_plan.filter(actual_pt_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="WH"):
		## bug here case of point two items the order of product is mess up
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_wh_start", "product_id", "actual_wh_start")
			item_current = list(today_plan.filter(actual_wh_start = None).values_list("product_id").order_by('plan_wh_start'))[0][0]
			#item_current = item.strftime("%H:%M")
		except IndexError, error:
			item_current = 'idle'
	return item_current

##################################
## get current time in schedule ##
##        return time           ##
##################################
def currentTimeProcess(machine):
	today=todayDate()
	if(machine=="CR"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).order_by('plan_cr_start').values_list("actual_cr_end")
			item_current = today_plan.filter(actual_cr_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	## top current for CV 
	if(machine=="CV"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	## current by machine
	if(machine == "3CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CS").values_list("plan_cv_start","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CL").values_list("plan_cv_start","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CL"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CL").values_list("plan_cv_start","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="3CW"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="3CW").values_list("plan_cv_start","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="2CS"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').filter(cv_machine="2CS").values_list("plan_cv_start","actual_cv_end")
			item_current = today_plan.filter(actual_cv_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="PT"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_pt_start__year=today.year, plan_pt_start__month=today.month, plan_pt_start__day=today.day).order_by('plan_pt_start').values_list("plan_pt_start","actual_pt_end")
			item_current = today_plan.filter(actual_pt_end = None).values_list("product_id")[0][0]
		except IndexError, error:
			item_current = 'idle'
	if(machine=="WH"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_wh_start__year=today.year, plan_wh_start__month=today.month, plan_wh_start__day=today.day).values_list("plan_wh_start","actual_wh_start").order_by('plan_wh_start')
			item_current = today_plan.filter(actual_wh_start = None).values_list("plan_wh_start")[0][0]
			#item_current = item.strftime("%H:%M")
		except IndexError, error:
			item_current = 'idle'
	return item_current	
######################################################
## get position of current process for each section ##
######################################################
def positionOfCurrentProcess(machine,product):
	today = todayDate()
	position = 0
	if(product == 'i'):
		position = -2
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
	if(machine == "3CW"):
		try:
			today_plan = FakeStatusTracking.objects.filter(plan_cv_start__year=today.year, plan_cv_start__month=today.month, plan_cv_start__day=today.day).order_by('plan_cv_start').values_list("product_id")
			for pos, item in enumerate(today_plan):
				if str(item)[2:8] == product:
					position = pos
		except IndexError, error:
			position = -1
	if(machine == "2CS"):
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
#################################
## return the starting pointer ##
##  when PC limits view items  ##
def returnStartingPoint(pos,length):
	limit = getPCItemNum()
	if pos == -2:
		return length-limit
	elif pos < limit:
		return 0
	elif pos > length - 4:
		return length-limit
	else :
		return pos-limit/2


