# Create your views here.
from django.shortcuts import render_to_response

def now(request):
	return render_to_response('now.html', locals())

