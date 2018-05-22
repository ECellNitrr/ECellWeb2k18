from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import jwt
import json
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings

@csrf_exempt
def post(request, *args, **kwargs):

	error_msg = {'status' : 400,
		'content_type' : 'application/json',
		'message' : 'Invalid credentials'}

	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		print(username)
		try:
			user = authenticate(username=username, password=password)
		except User.DoesNotExist:
			return JsonResponse(error_msg)
		if user:

			payload = {
				'id' : user.id,
				'email': user.email,
			}

			jwt_token = jwt.encode(payload,settings.SECRET_KEY)
			token = jwt_token.decode('utf-8')
			return JsonResponse({
				'status' : 200,
				'content_type' : 'application/json',
				'message' : 'authentication successfull',
				'token' : token
			})

		else:
			return JsonResponse(error_msg)
	return render(request,'login.html')
