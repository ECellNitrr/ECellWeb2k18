from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Message
from .forms import MessageForm

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

@csrf_exempt
#@login_req
def create_message(request,**kwargs):
	if request.method == 'POST':
		message_form = MessageForm(request.POST)

		if message_form.is_valid():

			message = message_form.save(commit=False)
			message.user_id = kwargs['user_id']
			message.save()
			message = model_to_dict(message)
			return JsonResponse({
				'success' : True,
				'message' : message
			})
		else:
				return JsonResponse({
						'success' :False,
						'message' : 'Invalid Form'
					})
	else:
		return JsonResponse({
			'success':False,
			'message':'Wrong method (Use POST)'
		})

@csrf_exempt
@login_req
def delete_message(request,id,**kwargs):
	message = Message.objects.get(id = id)
	if message.user_id == kwargs['user_id']:
		message.flag = False
		message.save()

		return JsonResponse({
			'success':True,
			'message':'Message Deleted successfully'
		})
	else:
		return JsonResponse({
			'success':False,
			'message':'Not Authorized to delete'
		})
@csrf_exempt
@login_req
def edit_message(request,id,**kwargs):
	message = Message.objects.get(id=id)
	if message.user_id == kwargs['user_id']:
		if request.method == 'POST':
			message_form = MessageForm(request.POST, instance=message)

			if message_form.is_valid():

				message.save()
				message = model_to_dict(message)
				return JsonResponse({
					'success' : True,
					'message' : message
				})
			else:
					return JsonResponse({
							'success' :False,
							'message' : 'Invalid Form'
						})
		else:
			return JsonResponse({
				'success':False,
				'message':'Wrong method (Use POST)'
			})
	else:
		return JsonResponse({
			'success':False,
			'message':'Not Authorized to edit'
		})
