#Author: Chanaphan Prasomwong
# Last updated: 25/03/2010 
# Purpose: this file is containing function
# for the first time entering to the site 
# and check authentication of the page access 

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import Template, Context
########################
## display login page ##
########################

def login(request):
	title = "Welcome to Likitomi Status Tracking System"
	flashMessage =""
	page ="login"
	la_user_name = "USERNAME"
	is_enable_tributton = False
	is_enable_leftbutton = False
	section_title = "Welcome"
	content_header = "Login"
	subcontent_header = "Please scan or enter employee code"
	item_pic = "thumbs/mail.png"
	item_name = "Item name"
	is_enable_link = False
	is_enable_comment = False
	is_enable_arrow = False
	is_enable_login = True
	return render_to_response('view.html', locals())

