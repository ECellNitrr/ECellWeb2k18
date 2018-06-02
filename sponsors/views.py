from .models import Sponsor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from server.decorators.login import login_req
from .forms import SponsorForm
import json

@csrf_exempt
def get_sponsors(request):
	sponsors = Sponsor.objects.all().values()
	sponsors_list = list(sponsors)
	return JsonResponse({
		'success':True,
		'Sponsor_List':sponsors_list
		})

@csrf_exempt
def view(request,id):
	sponsor = Sponsor.objects.filter(id=id).first()
	sponsor = model_to_dict(sponsor)
	sponsor['pic'] = str(sponsor['pic'])
	return JsonResponse({
		'success':True,
		'sponsor':sponsor
		},safe=False)

@csrf_exempt
@login_req
def create_spons(request):
	if request.method == "POST":
		sponsor_form = SponsorForm(request.POST,request.FILES)

		if sponsor_form.is_valid():

			sponsor = sponsor_form.save()
			sponsor.save()

			return JsonResponse({
				'success' : True,
				'message' : 'Sponsor addded successfully'
			})
		else:
				return JsonResponse({
						'success' :False,
						'message' : 'Invalid Form'
					})

	else:
		return JsonResponse({
				'success' :False,
				'message' : 'form method error'
			})

@csrf_exempt
@login_req
def delete_spons(request,id):
	sponsor = Sponsor.objects.get(id=id)
	if not sponsor:
		return JsonResponse({
			'success':False,
			'message':'Record not found'
			})
	else:
		sponsor.flag = False
		sponsor.save()
		return JsonResponse({
			'success':True,
			'message':'Record Deleted Succesfully'
			})

@csrf_exempt
@login_req
def edit_spons(request,id):
	if request.method == 'POST':
		name = request.POST.get('name')
		detail = request.POST.get('details')
		pic = request.FILES.get('pic')
		contact = request.POST.get('contact')
		website = request.POST.get('website')
		spons_type = request.POST.get('spons_type')
		try:
			sponsor = Sponsor.objects.get(id=id)
		except:
			return JsonResponse({
				'sucess':False,
				'message':'Record not found'
				})

		sponsor.name = name
		sponsor.details = detail
		sponsor.pic = pic
		sponsor.contact = contact
		sponsor.website = website
		sponsor.spons_type = spons_type
		sponsor.save()
		sponsor = model_to_dict(sponsor)
		sponsor['pic'] = str(sponsor['pic'])
		return JsonResponse({
				'success':True,
				'Sponsor':sponsor
		},safe=False)
	else:
		return JsonResponse({
			'sucess':False,
			'message':'Method Error'
		})
