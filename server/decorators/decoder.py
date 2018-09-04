from rest_framework import authentication, exceptions
from appprofile.models import Profile
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
import jwt
import json
from functools import wraps
from django.conf import settings as conf_settings

def decoder(function):
    def wrap(request, *args, **kwargs):
        
        token = request.META['HTTP_AUTHID']
        # if not auth_header:
        #     return JsonResponse({'success':False,'message':'Error at auth_header'})

        # if len(auth_header) == 1:
        #     return JsonResponse({'success':False,'message':'Error at auth_header2'})

        # elif len(auth_header) > 2:
        #     return JsonResponse({'success':False,'message':'Error at auth_header3'})
        # print("stage 1")
        # prefix = auth_header[0].decode('utf-8')
        # token = auth_header[1].decode('utf-8')
        # print("Stage 2")
        # if prefix.lower() != auth_header_prefix:
        #     return JsonResponse({'success':False,'message':'Error at auth_header_prefix'})
        # print("Stage 3")
        try:
            print("Trying to decode TOKEN: ", token)
            payload = jwt.decode(token, conf_settings.SECRET_KEY)
        except:
            print("Unable to decode token: ", token)
            msg = 'Invalid authentication. Could not decode token.'
            return JsonResponse({'success':False,'message':msg})
        try:
            print("Trying to find profile")
            user = Profile.objects.get(user_id=payload['id'])
        except Profile.DoesNotExist:
            print("Profile not found")
            msg = 'No user matching this token was found.'
            return JsonResponse({'success':False,'message':msg})
        kwargs['user_id'] = payload['id']
        kwargs['user_email'] = payload['email']
        
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
