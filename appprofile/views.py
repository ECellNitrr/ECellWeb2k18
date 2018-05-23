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



def register(request):

	registered = False

	if request.method == "POST":
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileInfoForm(request.POST,request.FILES)

		if user_form.is_valid() and profile_form.is_valid() :

			user = user_form.save()
			user.set_password(user.password)
			user.save()
			#profile_form.save()
			profile = profile_form.save()
			profile.user = user
			#profile_form.avatar = profile_form.cleaned_data['avatar']
			profile.save()

			#profile = profile_form.save()
			#profile.user = user


			#profile.avatar = profile_form.cleaned_data['avatar']
			#profile.doc_image = profile_form.cleaned_data['doc_image']
			#profile.save()
			#profile.first_name.save()

			registered = True

		else:
			print(user_form.errors, profile_form.errors)

	else:
		user_form = UserForm()
		profile_form = UserProfileInfoForm()

	return render(request,'register.html',
		                   {'user_form':user_form,
		                    'profile_form':profile_form,
		                    'registered':registered,
							})
