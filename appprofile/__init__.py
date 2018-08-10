import multiprocessing
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage


import jwt
import json
import http.client



def send_mail(email, user):

  
    mail_subject = "Activate your Ecell account"
    message = render_to_string('acc_active_email.html',{
        'user':user,
       
        'uid':urlsafe_base64_encode(force_bytes(user.pk)).decode(),
        'token':account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(mail_subject,message,to=[to_email])
    email.send()