from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Startup

@csrf_exempt
def get_startups(request):
	startups = Startup.objects.all().values()
	startups_list = list(startups)
	return JsonResponse({
		'success' : True,
		'startups': startups_list
		 },safe=False)

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
