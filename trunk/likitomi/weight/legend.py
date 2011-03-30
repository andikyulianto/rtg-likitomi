# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.db import connection, transaction
from weight.models import PaperRoll, PaperHistory

def legend(request):

	if 'pcode' in request.GET and request.GET['pcode']:
		pcode = request.GET['pcode']
	else:
		pcode = ""

	if 'width' in request.GET and request.GET['width']:
		width = request.GET['width']
	else:
		width = ""

	if 'loss' in request.GET and request.GET['loss']:
		loss = request.GET['loss']
		losspx = int(loss)/4
		if losspx > 250:
			losspx = 250
		losspxinv = 250-losspx
	else:
		loss = ""

	query = PaperRoll.objects.filter(paper_code=pcode, width=width).values_list('id')
	qexists = PaperRoll.objects.filter(paper_code=pcode, width=width).exists()

	if qexists == True:
		wlist = list()
		ridlist = list()
		lesslist = list()
		morelist = list()
		dlesslist = list()
		dmorelist = list()
		clesslist = list()
		cmorelist = list()

		for item in query:
			totem = list(item)
			rid = int(totem[0])
			ridlist.append(rid)
			exists = PaperHistory.objects.filter(roll_id=rid).exists()
			if exists == True:
				weight = int(str(PaperHistory.objects.filter(roll_id=rid).order_by('-timestamp').values_list('last_wt')[0])[1:][:-3])
			else:
				weight = int(str(PaperRoll.objects.filter(id=rid).values_list('initial_weight')[0])[1:][:-3])
			wlist.append(weight)
			wlist.sort()
		for w in wlist:
			if int(w) < int(loss): lesslist.append(w)
			else: morelist.append(w)
		for w in lesslist:
			if w not in dlesslist: dlesslist.append(w)
		for w in morelist:
			if w not in dmorelist: dmorelist.append(w)
		for w in dlesslist:
			c = lesslist.count(w)
			clesslist.append(c)
		for w in dmorelist:
			c = morelist.count(w)
			cmorelist.append(c)

		initial_weight = int(str(PaperRoll.objects.filter(paper_code=pcode).values_list('initial_weight')[0])[1:][:-3])

	return render_to_response('legend.html', locals())

