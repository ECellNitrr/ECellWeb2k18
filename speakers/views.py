from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Speaker
from django.shortcuts import render

@csrf_exempt
def get_speakers(request):
	speakers = Speaker.objects.all().values()
	speakers_list = list(speakers)
	return JsonResponse({
		'success':True,
		'speakers':speakers_list
		},safe=False)




def post_speakers(request):
	return render(request,'website/speakers.html')

@csrf_exempt
def view_speaker(request,id):
	speaker = Speaker.objects.filter(id = id).first()
	speaker = model_to_dict(speaker)
	speaker['profile_pic'] = str(speaker['profile_pic'])

	return JsonResponse({
		'success':True,
		'speaker':speaker
	})
