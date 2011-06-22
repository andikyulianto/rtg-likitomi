# Create your views here.
from weight.models import ClampliftPlan
from django.shortcuts import render_to_response
from datetime import datetime

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.conf import settings

def orient(request):
	return render_to_response('orient.html', locals())

def longtry(request):
	logging.basicConfig(filename='exceptions.log', level=logging.DEBUG)

	try:
		1/0
	except ZeroDivisionError as e:
		logging.debug(e)

	return render_to_response('longtry.html', locals())
