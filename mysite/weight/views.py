# Create your views here.
#from django.template.loader import get_template
from django.shortcuts import render_to_response
#from django.template import Template, Context
#from django.http import Http404, HttpResponse, HttpResponseRedirect
#from django.db import connection, transaction

#import datetime
#import serial
#import MySQLdb
#import Image
#import socket
#import StringIO
#import cStringIO
#import random

def index(request):
	return render_to_response('index.html', locals())

