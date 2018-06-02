from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Message

@csrf_exempt
def get_messages(request):
	messages = Message.objects.all().values()
	messages_list = list(messages)
	return JsonResponse({
		'success':True,
		'messages':messages_list
	}, safe=False)

@csrf_exempt
def view_message(request,id):
	message = Message.objects.filter(id = id).first()
	message = model_to_dict(message)
	return JsonResponse({
		'success':True,
		'message':message
	})
