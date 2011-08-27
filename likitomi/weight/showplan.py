from django.shortcuts import render_to_response
from datetime import date, time, datetime, timedelta

from weight.models import TblClamplift
#from statusTracking.models import TotalPlanning, Delivery, Products, ProductCatalog, Partners, StatusTracking

def showplan(request):
	"""
	Displays clamp-lift plan minimal version.

		Retrieve the minimal clamp-lift plan by the date selected from dashboard.

	**Context:**

	``Models``

		:model:`weight.TblClamplift`

	**Template:**

	:template:`templates/clamplift/showplan.html`

	"""

# Get date for querying clamp-lift plan
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	if opdate: 
		query = TblClamplift.objects.filter(opdate=opdate).values_list('start_time', 'product_code', 'autoid', 'p_width_inch', 'df', 'bl', 'bm', 'cl', 'cm', 'used_df_mkg', 'used_bl_mkg', 'used_bm_mkg', 'used_cl_mkg', 'used_cm_mkg')

	now = datetime.now()
	qlist = list(query)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('showplan.html', locals())

def required(request):
	"""
	Displays clamp-lift plan required set of detailed version.

		Retrieve the detailed clamp-lift plan with required set by the date selected from dashboard.

	**Context:**

	``Models``

		:model:`weight.TblClamplift`

	**Template:**

	:template:`templates/clamplift/required.html`

	"""

# Get date for querying clamp-lift plan
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	required = TblClamplift.objects.filter(opdate=opdate).values_list('start_time', 'product_code', 'sales_order', 'autoid', 'flute', 'df', 'bl', 'bm', 'cl', 'cm', 'p_width_mm', 'p_width_inch', 'used_df_mkg', 'used_bl_mkg', 'used_bm_mkg', 'used_cl_mkg', 'used_cm_mkg')

	now = datetime.now()
	qlist = list(required)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('required.html', locals())

def detail(request):
	"""
	Displays clamp-lift plan detailed set of detailed version.

		Retrieve the detailed clamp-lift plan with detailed set by the date selected from dashboard.

	**Context:**

	``Models``

		:model:`weight.TblClamplift`

	**Template:**

	:template:`templates/clamplift/detail.html`

	"""

# Get date for querying clamp-lift plan
	if 'opdate' in request.GET and request.GET['opdate']:
		opdate = request.GET['opdate']
	else:
		opdate = date.today().strftime("%Y-%m-%d")

	detail = TblClamplift.objects.filter(opdate=opdate).values_list('start_time', 'product_code', 'sales_order', 'autoid', 'partner_name', 'product_name', 'used_df', 'used_bl', 'used_bm', 'used_cl', 'used_cm', 'used_df_lkg', 'used_bl_lkg', 'used_bm_lkg', 'used_cl_lkg', 'used_cm_lkg', 't_length', 'case', 'cut')

	now = datetime.now()
	qlist = list(detail)
	nlist = list()
	for lst in qlist:
		nlst = list(lst)
		nlist.append(nlst)
	n = 0
	for lst in nlist:
		lst.append(n)
		n = n + 1
	tdelta = list()
	s_tdelta = list()
	for tup in qlist:
		delta = datetime(now.year,now.month,now.day,tup[0].hour,tup[0].minute)-now
		tdelta.append(int(delta.seconds))
		s_tdelta.append(int(delta.seconds))
	s_tdelta.sort()
	if tdelta:
		chosen = tdelta.index(s_tdelta[0])
		scroll = chosen*84

	return render_to_response('detail.html', locals())

