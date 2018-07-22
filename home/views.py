from django.shortcuts import render

from .models import Msg

msg = True

def homepage(request):
    return render(request, 'website/index.html')

def message(request):
    post = request.POST
    msg = Msg(name=post['name'],email=post['email'],msg=post['msg'])
    msg.save()
