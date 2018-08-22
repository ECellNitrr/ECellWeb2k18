from .models import Sponsor
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from server.decorators.login import login_req
from .forms import SponsorForm
import json
from django.shortcuts import render
from django.utils.six.moves.urllib.parse import urlsplit
from decouple import config

@csrf_exempt
def get_sponsors(request):
	response = {}
	sponsors = Sponsor.objects.all().values()
	scheme = urlsplit(request.build_absolute_uri(None)).scheme
	if Sponsor.objects.filter(flag=True).exists():
		response['success'] = True
		AS = Sponsor.objects.filter(spons_type='AS').values()
		for spons in AS:
			# sponsor['pic'] = scheme+'://'+request.META['HTTP_HOST']+'/'+str(sponsor['pic'])
			spons['pic'] = config('HOST')+str(spons['pic'])
		PLTS =Sponsor.objects.filter(spons_type='PLTS').values()
		for spons in PLTS:
			spons['pic'] = config('HOST')+str(spons['pic'])
		GS = Sponsor.objects.filter(spons_type='GS').values()
		for spons in GS:
			spons['pic'] = config('HOST')+str(spons['pic'])
		TS = Sponsor.objects.filter(spons_type='TS').values()
		for spons in TS:
			spons['pic'] = config('HOST')+str(spons['pic'])
		PRTS = Sponsor.objects.filter(spons_type='PRTS').values()
		for spons in PRTS:
			spons['pic'] = config('HOST')+str(spons['pic'])
		AS_list = list(AS)
		PLTS_list = list(PLTS)
		GS_list = list(GS)
		TS_list = list(TS)
		PRTS_list = list(PRTS)
		spons = [ {'section_name':'Associate Sponsors', "sponsors":AS_list},
			  {'section_name':'Platinum Sponsors', "sponsors":PLTS_list},
			  {'section_name':'Gold Sponsors', "sponsors":GS_list},
			  {'section_name':'Title Sponsors', "sponsors":TS_list},
			  {'section_name':'Partner Sponsors', "sponsors":PRTS_list},
			]
		response['spons'] = spons
	else:
		response['success'] = False
		response['message'] = "Coming soon"

	return JsonResponse(response)


def post_sponsors(request):
	return render(request,'website/patreons.html')

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
def create_spons(request,**kwargs):
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
def delete_spons(request,id,**kwargs):
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
def edit_spons(request,id,**kwargs):
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
				'success':False,
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
				'sponsor':sponsor
		},safe=False)
	else:
		return JsonResponse({
			'sucess':False,
			'message':'Method Error'
		})
