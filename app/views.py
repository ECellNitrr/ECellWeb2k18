from django.shortcuts import render
from .models import App
from django.http import JsonResponse
from .models import App

def get_app(request):
	app_ver = app.objects.all().values()
	app_ver_list = list(app_ver)
	return JsonResponse(app_ver_list, safe=False)

def latest_build(request):
	response = {}
	if(App.objects.filter(flag=True).exists()):
		response['success'] = True
		app = App.objects.get(flag=True)
		response['version'] = app.version
		response['url'] = app.link
		response['message'] = app.log
	else:
		response['success'] = False
		response['message'] = 'Sorry no updates available'
	return JsonResponse(response)