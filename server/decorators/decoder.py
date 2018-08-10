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
        authentication_header_prefix = 'Token'

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = authentication_header_prefix.lower()

        if not auth_header:
            return JsonResponse({'success':False,'msg':'Error at auth_header'})

        if len(auth_header) == 1:
            return JsonResponse({'success':False,'msg':'Error at auth_header2'})

        elif len(auth_header) > 2:
            return JsonResponse({'success':False,'msg':'Error at auth_header3'})

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return JsonResponse({'success':False,'msg':'Error at auth_header_prefix'})

        try:
            payload = jwt.decode(token, conf_settings.SECRET_KEY)
        except:
            msg = 'Invalid authentication. Could not decode token.'
            return JsonResponse({'success':False,'message':msg})

        try:
            user = Profile.objects.get(pk=payload['id'])
        except Profile.DoesNotExist:
            msg = 'No user matching this token was found.'
            return JsonResponse({'success':False,'message':msg})
        kwargs['user_id'] = payload['id']
        kwargs['user_email'] = payload['email']
        
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
