from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.db.models import Q
from datetime import date
from app.models import Employee, FakeStatusTracking


def start(request):
	eID = request.GET['eID']
	planID = request.GET['pID']
	today = todayDate()
	#plan = Employee.objects.get(eid=eID)
	plan = FakeStatusTracking.objects.get(plan_id = planID )
	product = plan.product_id
	return render_to_response('updateCR1.html', locals())
def todayDate():
	tempDate = date(2010,11,19)
	return tempDate

