from django.http import HttpResponse
from django.shortcuts import render_to_response
from app.models import Employee, FakeStatusTracking
def view(request):
	eID = request.GET['eID']
	productDetail = request.GET['pCode']
	return render_to_response('product.html', locals())
