# Create your views here.
from weight.models import ClampliftPlan
from django.shortcuts import render_to_response
from datetime import datetime

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def orient(request):
	return render_to_response('orient.html', locals())

def longtry(request):
	longtry = 'longtry'

	return render_to_response('longtry.html', locals())
