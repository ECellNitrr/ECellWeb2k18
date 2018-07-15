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
	team = {}
	executive = Member.objects.filter(member_type ='EXEC').values()
	executive = list(executive)
	#executive['image'] =str(executive['image'])
	#print(executive)
	

	manager = Member.objects.filter(member_type = 'MNG').values()
	manager = list(manager)
	

	
	OverallCoordinator = Member.objects.filter(member_type = 'OC').values()
	OverallCoordinator = list(OverallCoordinator)
	#OverallCoordinator['image'] =str(OverallCoordinator['image'])

	HeadCoordinator = Member.objects.filter(member_type = 'HC').values()
	HeadCoordinator = list(HeadCoordinator)
	#HeadCoordinator['image'] =str(HeadCoordinator['image'])

	FacultyIncharge = Member.objects.filter(member_type = 'Fclty').values()
	FacultyIncharge = list(FacultyIncharge)
	#FacultyIncharge['image'] =str(FacultyIncharge['image'])

	HeadCareer = Member.objects.filter(member_type = 'HCD').values()
	HeadCareer = list(HeadCareer)
	#DeanResearch['image'] =str(DeanResearch['image'])

	Director= Member.objects.filter(member_type = 'Dir').values()
	Director = list(Director)
	#Director['image'] =str(Director['image'])

	team = { 	 
            'Director, NIT Raipur':Director,
			'Head of Career development':HeadCareer,
            'Faculty Incharge':FacultyIncharge,
            'Head Co-ordinator':HeadCoordinator ,
            'Overall Co-ordinator':OverallCoordinator,
            'manager' : manager,
            'executive':executive,
        }

	return JsonResponse(team, safe=False)
    
def team_site(request):
    return render(request, 'website/team.html')