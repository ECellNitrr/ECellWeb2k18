from django.shortcuts import render

# Create your views here
import jwt
import json
from django.http import HttpResponse, JsonResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
#from rest_framework import api_view



def post(request, *args, **kwargs):
	if request.method=='POST':
		print('uy')
		#if not request.:
		#	return HttpResponse('Error please provide username/password')
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		try:
			#user = User.objects.get(username=username)
			user = authenticate(username=username, password=password)
		except User.DoesNotExist:
			return HttpResponse('Invalid username/password')
		if user:

			payload = {
				'id' : user.id,
				'email': user.email,
			}

			jwt_token = {'token':jwt.encode(payload,"SECRET_KEY")}
			#jwt_token = list(jwt_token)
			print(jwt_token)
			return JsonResponse(jwt_token, safe=False)

			#return HttpResponse(json.dumps(jwt_token),
							#	status = 200,
							#	content_type='application/json')
		else:
			return Response(
				json.dumps({'Error':'Invalid credentials'}),
				status=400,
				content_type='application/json')
		#if request.method=='POST':	
		#	post(self, request, *args, **kwargs)




	return render(request,'login.html')
