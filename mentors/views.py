from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .models import Mentor

@csrf_exempt
def get_mentors(request):
    mentors = Mentor.objects.all().values()
    mentors = list(mentors)
    return JsonResponse({
            'success':True,
            'mentors':mentors
        }, safe=False)

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
