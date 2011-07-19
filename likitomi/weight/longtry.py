# Create your views here.
from weight.models import TblClamplift
from django.shortcuts import render_to_response
from datetime import datetime

# import the logging library
import logging
import traceback

# Get an instance of a logger
logger = logging.getLogger(__name__)

from django.conf import settings

def orient(request):
	return render_to_response('orient.html', locals())

def longtry(request):
	logging.basicConfig(filename='/home/patipol/rtg-likitomi/likitomi/static/logfile.log', level=logging.DEBUG)

	try:
		1/0
	except ZeroDivisionError as e:
		logging.error(str(e) +" by requesting \"./longtry/\" at "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		logging.error(traceback.print_exc())

	return render_to_response('longtry.html', locals())
