from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from statusTracking.models import Employee, FakeStatusTracking
def queryDateNotProcess(request):
	eID = request.GET['eID']
	datefrom = request.GET['from']
	dateto = request.GET['to']

	today = todayDate()
	temp_contents = ''
	title = str(today)
	employee = Employee.objects.get(eid=eID)
	page =  employee.task
	datefrom = datetime.date(2007, 12, 5)
	dateto = datetime.date(2011,28, 
	notProcessCR = FakeStatusTracking.objects.filter(plan_cr_start__year= today.year, plan_cr_start__month=today.month, plan_cr_start__day=today.day).values_list("plan_cr_start","plan_cr_end","product_id","actual_cr_start","actual_cr_end","days_left","plan_amount","actual_amount_cr").order_by('plan_cr_start')
	
	return render_to_response('home.html', locals())
