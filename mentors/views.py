from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Mentor
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config

@csrf_exempt
def get_mentors(request):
    response = {}
    if Mentor.objects.filter(flag=True).exists():
        mentors = Mentor.objects.all().values()
        scheme = urlsplit(request.build_absolute_uri(None)).scheme
        for m in mentors:
            m['profile_pic'] = config('HOST')+str(m['profile_pic'])
        mentors = list(mentors)
        response['success'] = True
        response['mentors'] = mentors
    else:
        response['success'] = False
        response['message'] = "Coming Soon"
    return JsonResponse(response)


def post_mentors(request):
    return render(request,'website/mentors.html')


@csrf_exempt
def view_mentor(request, id):
    try:
        mentor = Mentor.objects.filter(id=id).first()
    except:
        return JsonResponse({
            'sucess':False,
            'message':'No Mentor found with such id'
            })
    mentor = model_to_dict(mentor)
    mentor['profile_pic'] = str(mentor['profile_pic'])
    return JsonResponse({
            'success':True,
            'mentor' : mentor
            })
