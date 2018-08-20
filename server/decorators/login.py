from rest_framework import authentication, exceptions
from appprofile.models import Profile
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
import jwt
import json
from functools import wraps
from decouple import config

def login_req(function):
    def wrap(request, *args, **kwargs):
        token = request.META['HTTP_AUTHID']
        try:
            print("Trying to decode TOKEN")
            print(token)
            payload = jwt.decode(token, config('SECRET_KEY'))
        except:
            print("Unable to decode")
            msg = 'Invalid authentication. Could not decode token.'
            return JsonResponse({'success':False,'message':msg})
        try:
            print("Trying to find profile")
            user = Profile.objects.get(pk=payload['id'])
        except Profile.DoesNotExist:
            print("Profile not found")
            msg = 'No user matching this token was found.'
            return JsonResponse({'success':False,'message':msg})
        
        if user.status is False:
            return JsonResponse({'success':False,'message':'Your Account hasn\'t been activated yet.'})
            
        kwargs['user_id'] = payload['id']
        user.is_active = True;
        #login(request,user)
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap