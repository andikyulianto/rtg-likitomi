# Create your views here.
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.template import Template, Context
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.db import connection, transaction

#from time import localtime, gmtime, ctime
#from datetime import datetime, date

def now(request):
#	try:
#		local = localtime()
#		gmt = gmtime()
#		rightnow = datetime(*local[:6])
#		thistime = rightnow.strftime("%H:%M:%S")

#	except:
#		pass

	return render_to_response('now.html', locals())

