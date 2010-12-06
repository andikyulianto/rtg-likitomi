from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context

def index(request):
	title = "Welcome to Likitomi Status Tracking System"
	is_enable_tributton = False
	is_enable_leftbutton = False
	section_title = "Welcome"
	content_header = "Login"
	subcontent_header = "Please scan or enter employee code"
	item_pic = "thumbs/mail.png"
	item_name = "Item name"
	item_link = "http://www.google.com"
	is_enable_link = False
	is_enable_comment = False
	is_enable_arrow = False
	is_enable_login = True
	return render_to_response('index.html', locals())

def login(request):
	title = "This is title"
	return render_to_response('index.html', locals())
#def login(request):
#	fp = open('/home/fon/Django-123/projects/likitomi/templates/index.html')
#	t = Template(fp.read())
#	fp.close()
#	html = t.render(Context({'title': "This is title"}))
#	return HttpResponse(html)
	
