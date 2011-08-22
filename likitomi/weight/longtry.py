# Create your views here.
from weight.models import TblClamplift
from statusTracking.models import TotalPlanning, Delivery, Products, ProductCatalog, Partners, StatusTracking
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
	query = TblClamplift.objects.filter(opdate="2011-08-20").values_list('start_time', 'product_code', 'autoid', 'p_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'used_df_mkg', 'used_bl_mkg', 'used_bm_mkg', 'used_cl_mkg', 'used_cm_mkg')

	logging.basicConfig(filename='/home/patipol/rtg-likitomi/likitomi/static/logfile.log', level=logging.DEBUG)

	try:
		1/0
	except ZeroDivisionError as e:
		logging.error(str(e) +" by requesting \"./longtry/\" at "+ datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
		logging.error(traceback.print_exc())

	return render_to_response('longtry.html', locals())
