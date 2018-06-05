from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.conf import settings
from .forms import UserForm, UserProfileInfoForm
from django import forms

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth.hashers import make_password

import jwt
import json


@csrf_exempt
def login(request, *args, **kwargs):

	error_msg = {
		'success' : False,
		'message' : 'Invalid credentials'
		}

	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		


		try:
			usernm = User.objects.get(username=username).username
			user = authenticate(username=usernm, password=password)
			#print(user)
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
				'success' : True,
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

		if user_form.is_valid() and profile_form.is_valid():

			user = user_form.save()
			user.set_password(user.password)
			user.is_active=False;
			user.save()

			user.profile.avatar = profile_form.cleaned_data.get('avatar')
			user.profile.contact_no = profile_form.cleaned_data.get('contact_no')
			user.profile.facebook = profile_form.cleaned_data.get('facebook')
			user.profile.linkedin = profile_form.cleaned_data.get('linkedin')
			user.profile.status=0
			user.profile.save()
			#------------------
			current_site = get_current_site(request)
			mail_subject = "Activate your Ecell account"
			message = render_to_string('acc_active_email.html',{
				'user':user,
				'domain':current_site.domain,
				'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
				'token':account_activation_token.make_token(user),
			})
			to_email = user.email
			email = EmailMessage(mail_subject,message,to=[to_email])
			email.send()
			#------------------
			return JsonResponse({
				'success' : True,
				'message' : 'registration successfull'
			})
		else:
				return JsonResponse({
						'success' :False,
						'User Form Errors' : user_form.errors.as_json(),
						'Profile Form Errors' : profile_form.errors.as_json(),
						'message':'Invalid Form'
					})

	else:
		return JsonResponse({
				'success' :False,
				'message' : 'form method error'
			})

@csrf_exempt
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.profile.status=1
        user.is_active = True
        user.save()
        return JsonResponse({'success':True,'message':'Account Activated Successfully'})
    else:
        return JsonResponse({'success':False,'message':'Activation link is invalid!'})
