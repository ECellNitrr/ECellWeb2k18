from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from .models import Member
from django.utils.six.moves.urllib.parse import urlsplit

# Create your views here.

def get_team(request):
	scheme = urlsplit(request.build_absolute_uri(None)).scheme
	member = Member.objects.all().values()
	for m in member:
		m['image'] = scheme+'://'+request.META['HTTP_HOST']+'/'+str(m['image'])
	member_list = list(member)
	Faculty = Member.objects.filter(member_type = 'Dir').values()  | Member.objects.filter( member_type='HCD').values() | Member.objects.filter(member_type = 'Fclty').values()
	for f in Faculty:
		f['image'] = scheme+'://'+request.META['HTTP_HOST']+'/'+str(f['image'])
	Faculty= list(Faculty)

	student_list = [item for item in member_list if item not in Faculty]

	response = {'success':True, 'message':'Team Members are available','Faculty':Faculty, 'Student':student_list}
	return JsonResponse(response, safe=False)

def team_site(request):
    return render(request, 'website/team.html')
