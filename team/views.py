from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json
from django.shortcuts import render
from .models import Member

# Create your views here.

def get_team(request):
	member = Member.objects.all().values()
	member_list = list(member)
	print(member_list)
	response = {'success':True, 'message':'Team Members are available','team_members': member_list}
	print(response)


	return JsonResponse(response, safe=False)
    
def team_site(request):
    return render(request, 'website/team.html')