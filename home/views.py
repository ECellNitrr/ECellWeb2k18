from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Msg

def homepage(request):
    return render(request, 'website/index.html')

def message(request):
    post = request.POST
    msg = Msg(name=post['name'],email=post['email'],msg=post['msg'])
    print('')
    msg.save()

    return render(request, 'website/index.html')
