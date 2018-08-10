from rest_framework import authentication, exceptions
from appprofile.models import Profile
from django.http import JsonResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
import jwt
import json
from functools import wraps

def login_req(function):
    def wrap(request, *args, **kwargs):
        authentication_header_prefix = 'Token'
        request.user = None

        auth_header = authentication.get_authorization_header(request).split()
        auth_header_prefix = authentication_header_prefix.lower()

        if not auth_header or len(auth_header) == 1 or len(auth_header) > 2:
            return JsonResponse({'success':False,'message':'Bad Authorization', 'status':401})

        prefix = auth_header[0].decode('utf-8')
        token = auth_header[1].decode('utf-8')

        if prefix.lower() != auth_header_prefix:
            return JsonResponse({'success':False,'message':'Bad Authorixation', status:401})

        try:
            payload = jwt.decode(token, settings.SECRET_KEY)
        except:
            message = 'Invalid authentication. Could not decode token.'
            return JsonResponse({'success':False,'message':message})

        try:
            user = Profile.objects.get(pk=payload['id'])
        except Profile.DoesNotExist:
            message = 'No user matching this token was found.'
            return JsonResponse({'success':False,'message':message})

        #if not Profile.is_active:
        #    message = 'This user has been deactivated.'
        #    return JsonResponse({'success':False,'message':message})
        kwargs['user_id'] = payload['id']
        user.is_active = True;
        #login(request,user)
        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap