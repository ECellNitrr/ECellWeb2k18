from django.shortcuts import render
from .models import Message
from django.http import JsonResponse
# Create your views here.

def get_messages(request):
	messages = Message.objects.all().values()
	messages_list = list(messages)
	return JsonResponse(messages_list, safe=False)
