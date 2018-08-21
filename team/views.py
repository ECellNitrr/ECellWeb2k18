from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from .models import Member
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config

# Create your views here.

def get_team(request):
	scheme = urlsplit(request.build_absolute_uri(None)).scheme
	member = Member.objects.filter(member_type = 'OC').values()
	for m in member:
		m['image'] = config('HOST')+str(m['image'])
	member_list = list(member)
	member = Member.objects.filter(member_type = 'HC').values()
	for m in member:
		m['image'] = config('HOST')+str(m['image'])
	member_list.append(list(member))
	member = Member.objects.filter(member_type = 'MNG').values()
	for m in member:
		m['image'] = config('HOST')+str(m['image'])
	member_list.append(list(member))
	member = Member.objects.filter(member_type = 'EXEC').values()
	for m in member:
		m['image'] = config('HOST')+str(m['image'])
	member_list.append(list(member))
	Faculty = Member.objects.filter(member_type = 'Dir').values()  | Member.objects.filter( member_type='HCD').values() | Member.objects.filter(member_type = 'Fclty').values()
	for f in Faculty:
		f['image'] = config('HOST')+str(f['image'])
	Faculty= list(Faculty)

	student_list = [item for item in member_list if item not in Faculty]
	if len(member_list)==0 and len(student_list)==0:
		return JsonResponse({'success':False, 'message':'Error! No Data available in Database'})	
	response = {'success':True, 'message':'Team Members are available','faculty':Faculty, 'student':student_list}
	return JsonResponse(response, safe=False)

def team_site(request):
    return render(request, 'website/team.html')
