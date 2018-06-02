from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

import jwt
import json
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from .forms import UserForm, UserProfileInfoForm


@csrf_exempt
def login(request, *args, **kwargs):

	error_msg = {'status' : 400,
		'content_type' : 'application/json',
		'message' : 'Invalid credentials'}

	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			user = authenticate(username=username, password=password)
		except User.DoesNotExist:
			return JsonResponse(error_msg)

		if user:

			user.is_active=True;
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


@csrf_exempt
def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(request.POST,request.FILES)

		if user_form.is_valid() and profile_form.is_valid() :

			user = user_form.save()
			user.set_password(user.password)
			user.save()

			user.profile.avatar = profile_form.cleaned_data.get('avatar')
			user.profile.contact_no = profile_form.cleaned_data.get('contact_no')
			user.profile.facebook = profile_form.cleaned_data.get('facebook')
			user.profile.linkedin = profile_form.cleaned_data.get('linkedin')
			user.profile.save()

			registered = True
			return JsonResponse({
				'status' : 200,
				'content_type' : 'application/json',
				'message' : 'registration successfull'
			})
		else:
				return render({
						'status' :400,
						'content_type' : 'application/json',
						'message' : 'Invalid Form'
					})

	else:
		return render({
				'status' :400,
				'content_type' : 'application/json',
				'message' : 'form method error'
			})
