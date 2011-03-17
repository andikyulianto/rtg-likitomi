from django.http import HttpResponse
from django.shortcuts import render_to_response
#from django.template import Template, Context

def playandtry(request):
	eID = "2A"
	listProduct = ["11", "12", "13", "14", "15"]
	return render_to_response('product_list.html', locals())
def display(request):
	listProduct = request.GET['listProduct']
	return render_to_response('productDetail.html',locals())

