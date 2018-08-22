from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Speaker
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config

@csrf_exempt
def get_speakers(request):
	response = {}
	if Speaker.objects.filter(flag=True).exists():
		speakers = Speaker.objects.all().values()
		scheme = urlsplit(request.build_absolute_uri(None)).scheme
		for speaker in speakers:
			speaker['profile_pic'] = config('HOST')+str(speaker['profile_pic'])
		speakers_list = list(speakers)
		response['success'] = True
		speakers_list = sorted(speakers_list, key=lambda i:i['year'], reverse=True)
		response['speakers'] = speakers_list
	else:
		response['success'] = False
		response['message'] = "Coming Soon"
	return JsonResponse(response)


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
