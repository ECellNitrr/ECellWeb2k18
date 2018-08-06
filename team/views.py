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

	Faculty = Member.objects.filter(member_type = 'Dir').values()  | Member.objects.filter( member_type='HCD').values() | Member.objects.filter(member_type = 'Fclty').values() 
	Faculty= list(Faculty)


	#print(Faculty)



	student_list = [item for item in member_list if item not in Faculty]

	#print(student_list)

	"""
	Dir = Member.objects.filter(member_type= 'Dir').values()
	HCD = Member.objects.filter(member_type= 'HCD').values()
	"""
	#FacultyIncharge['image'] =str(FacultyInch






	#print(member_list)
	response = {'success':True, 'message':'Team Members are available','Faculty':Faculty, 'Student':student_list}
	#print(response)


	return JsonResponse(response, safe=False)
    
def team_site(request):
    return render(request, 'website/team.html')