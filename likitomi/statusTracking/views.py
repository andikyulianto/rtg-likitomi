from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login

def login_user(request):
	try:
		flashMessage = request.GET['flashmess']
	except:
		flashMessage = ""
	content_header = "Login"
	
	title = "Welcome to Likitomi Status Tracking System"

	page ="login"

	is_enable_tributton = False
	is_enable_leftbutton = False
	section_title = "Welcome"
	content_header = "Login"
	subcontent_header = "Please scan or enter employee code"
	

	return render_to_response('auth.html',locals())
