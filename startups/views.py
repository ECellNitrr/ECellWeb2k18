from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Startup
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config

@csrf_exempt
def get_startups(request):
	startups = Startup.objects.all().values()
	scheme = urlsplit(request.build_absolute_uri(None)).scheme
	for startup in startups:
		# startup['pic'] = scheme+'://'+request.META['HTTP_HOST']+'/'+str(startup['pic'])
		startup['pic'] = config('HOST')+str(startup['pic'])
	startups_list = list(startups)
	if len(startups_list)==0:
		return JsonResponse({
		'success' : False,
		'message': 'Error! No Data Available in Database'
		 },safe=False)
	return JsonResponse({
		'success' : True,
		'startups': startups_list
		 },safe=False)

def post_startups(request):
	return render(request,'startup.html')

@csrf_exempt
def view_startup(request,id):
	try:
		 startup = Startup.objects.filter(id=id).first()
	except:
		return JsonResponse({
			'success':False,
			'message':'No Startup with such ID'
		})
	startup = model_to_dict(startup)
	startup['pic'] = str(startup['pic'])
	return JsonResponse({
		'success':True,
		'startup':startup
	})
