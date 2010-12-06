from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from datetime import date
from app.models import Employee, FakeStatusTracking

def report(request):
	eID = request.GET['eID']
	today = todayDate()
	content_header = "The list of date : " + today
	is_enable_table = True
	is_enable_desktop = True
	employee = Employee.objects.get(eid=eID)
	title = "Production Plan for "+employee.task
	section_title = "Homepage for " + employee.task + " Login as " + employee.firstname + " " + employee.lastname	
	if(employee.task == "PC"):
		getPCPlan()
#		item_plan = FakeStatusTracking.objects.filter(plan_cr_start__year=2010, plan_cr_start__month=11, plan_cr_start__day=19).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')[0:3]
#		item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=2010, plan_cv_start__month=11, plan_cv_start__day=19).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')[0:3]
#		item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=2010, plan_pt_start__month=11, plan_pt_start__day=19).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')[0:3]
#		item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=2010, plan_wh_start__month=11, plan_pt_start__day=19).values_list("plan_wh_start", "product_id", "actual_wh_start", "actual_wh_end").order_by('plan_wh_start')[0:3]
#		items_plan_cv = list(item_plan_cv)
#		items_plan_pt = list(item_plan_pt)
#		items_plan_wh = list (item_plan_wh)
#	items = list(item_plan)
	page_section = employee.task
	return render_to_response('home.html', locals())

def todayDate():
	date = str("2010-11-19")
	return date
def getPCPlan():
	item_plan_cr = FakeStatusTracking.objects.filter(plan_cr_start__year=2010, plan_cr_start__month=11, plan_cr_start__day=19).values_list("plan_cr_start", "plan_cr_end", "product_id", "actual_cr_start", "actual_cr_end").order_by('plan_cr_start')[0:3]
	item_plan_cv = FakeStatusTracking.objects.filter(plan_cv_start__year=2010, plan_cv_start__month=11, plan_cv_start__day=19).values_list("plan_cv_start", "plan_cv_end", "product_id", "actual_cv_start", "actual_cv_end", "cv_machine", "previous_section").order_by('plan_cv_start')[0:3]
	item_plan_pt = FakeStatusTracking.objects.filter(plan_pt_start__year=2010, plan_pt_start__month=11, plan_pt_start__day=19).values_list("plan_pt_start", "plan_pt_end", "product_id", "actual_pt_start", "actual_pt_end").order_by('plan_pt_start')[0:3]
	item_plan_wh = FakeStatusTracking.objects.filter(plan_wh_start__year=2010, plan_wh_start__month=11, plan_pt_start__day=19).values_list("plan_wh_start", "product_id", "actual_wh_start", "actual_wh_end").order_by('plan_wh_start')[0:3]
	items_plan_cv = list(item_plan_cv)
	items_plan_pt = list(item_plan_pt)
	items_plan_wh = list (item_plan_wh)
	items_plan_cr = list (item_plan_cr)
	
	return render_to_response('home.html', locals())
#class Plan:
#    def __init__(self,todayDate='',task='',planID=''):
#        self.planDate = todayDate
#        self.machineName = task
#        self.planID = self.setPlanID()
#        self.planStart =''
#        self.planEnd =''
#        self.planAmount = ''
#    def setPlanID(self):
#    	self.planID = FakeStatusTracking.objects.get(plan_id=1)
#    	return self.planID
#    def setMachineName(self,newMachineName):
#        self.machineName = newMachineName
#    def getMachineName(self):
#    	FakeStatusTracking.objects.get()
#        return self.machineName
#	def getPlanDate(self)= 1)
#    	return self.planID:
#		return self.planDate
#    def getPlanStart(self):
#        planObj = FakeStatusTracking.objects.get(plan_id=self.planID)
#        print planObj
#    def getPlanId(self):
#        return self.planID
#    def printPlan(self):
#        #print 'plan:',planID,'machine:',machineName,'start: ',planStart,'end: ',planEnd,'amount: ',planAmount
#        print 'plan:',self.PlanID

