from django.http import HttpResponse
def view(request):
	return render_to_response('index.html', locals())

