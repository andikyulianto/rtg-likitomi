from django.shortcuts import render_to_response

from weight.models import TblClamplift, PaperRolldetails

def dashboard(request):
	"""
	Dashboard of the Clamp-lift Application.

		Query date list for clamp-lift plan.

		Query paper code list and paper size list for search menu.

	**Context:**

	``Models``

		:model:`weight.TblClamplift`

		:model:`weight.PaperRolldetails`

	**Template:**

	:template:`templates/clamplift/dashboard.html`

	"""

# Query date list for plan #
	dquery = TblClamplift.objects.values_list('opdate').distinct().order_by('-opdate')

	dlen = len(dquery)
	if len(dquery) == 1:
		dstr = str(dquery)[16:][:-5]
	else:
		dstr = str(dquery)[16:][:-4]
	dsplt = dstr.split('),), (datetime.date(')
	datelist = list()
	for date in dsplt:
		datefrm = date.replace(", ","-")
		datelist.append(datefrm)

# Query paper code and size for search menu #
	spcode = PaperRolldetails.objects.values_list('paper_code').distinct().order_by('paper_code')
	spcodelist = list()
	for pcode in spcode:
		spcodelist.append(pcode[0])

	swidth = PaperRolldetails.objects.values_list('size').distinct().order_by('size')
	swidthlist = list()
	for width in swidth:
		swidthlist.append(width[0])

	return render_to_response('dashboard.html', locals())

