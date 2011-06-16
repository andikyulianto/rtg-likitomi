# Create your views here.
from weight.models import ClampliftPlan
from django.shortcuts import render_to_response
import datetime

def orient(request):
	return render_to_response('orient.html', locals())

def longtry(request):
#	query = ClampliftPlan.objects.filter(date='2010-03-30').values_list('start_time', 'sheet_code', 'paper_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'loss_df', 'loss_bl', 'loss_bm', 'loss_cl', 'loss_cm')

#	qlist = list(query)
#	nlist = list()
#	for lst in qlist:
#		nlst = list(lst)
#		nlist.append(nlst)

	query = ClampliftPlan.objects.filter(date='2010-03-30')

	return render_to_response('longtry.html', locals())
