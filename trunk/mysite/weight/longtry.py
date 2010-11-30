# Create your views here.
from weight.models import ClampliftPlan
from django.shortcuts import render_to_response
import datetime

def orient(request):
	return render_to_response('orient.html', locals())

def longtry(request):
	p = ClampliftPlan.objects.values_list('start_time', 'end_time', 'sheet_code')

	return render_to_response('longtry.html', locals())
