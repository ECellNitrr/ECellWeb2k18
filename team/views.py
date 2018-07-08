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

	DeanResearch = Member.objects.filter(member_type = 'DnRC').values()
	DeanResearch = list(DeanResearch)
	#DeanResearch['image'] =str(DeanResearch['image'])

	DeanStudent = Member.objects.filter(member_type = 'DnSW').values()
	DeanStudent = list(DeanStudent)
	#DeanStudent['image'] =str(DeanStudent['image'])


	Director= Member.objects.filter(member_type = 'Dir').values()
	Director = list(Director)
	#Director['image'] =str(Director['image'])

<<<<<<< HEAD
	team = { 	 
            'Director, NIT Raipur':Director,
            'Dean Student Welfare':DeanStudent,
            'Dean Research & Cons.':DeanResearch,
            'Faculty Incharge':FacultyIncharge,
            'Head Co-ordinator':HeadCoordinator ,
            'Overall Co-ordinator':OverallCoordinator,
            'manager' : manager,
            'executive':executive,
        }

	return JsonResponse(team, safe=False)
    
def team_site(request):
    return render(request, 'website/team.html')
=======
	team = { 	 'Director, NIT Raipur':Director,
				 'Dean Student Welfare':DeanStudent,
				 'Dean Research & Cons.':DeanResearch,
				 'Faculty Incharge':FacultyIncharge,
				 'Head Co-ordinator':HeadCoordinator ,
				 'Overall Co-ordinator':OverallCoordinator,
				 'manager' : manager,
				 'executive':executive,}

	



	return JsonResponse(team, safe=False)
>>>>>>> 81cdb9c8421ab187806be8f969045707294e7b34
