from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .forms import EventForm
from .models import Event
import json
from django.shortcuts import render

@csrf_exempt
def get_event(request):
    events= Event.objects.all().values()
    events_list=list(events)

    return JsonResponse({'sucess':True,'Events':events_list}, safe=False)



def post_event(request):
	return render(request,'event.html')



















@login_req
@csrf_exempt
def event_detail(request,pk):
	event = Event.objects.get( pk=pk)



	events = model_to_dict(event, fields=['name', 'venue','details','date', 'time', 'email','flag'])

	events['cover_pic'] = str(event.cover_pic)
	events['icon'] = str(event.icon)

	return JsonResponse({'Event':events}, safe=False)

@csrf_exempt
@login_req
def delete_event(request,pk,**kwargs):
	event = Event.objects.get(pk=pk)

	if not event:
		return JsonResponse({
			'success':False,
			'message':'Record not found'
			})
	else:
		event.flag = False
		event.save()
		return JsonResponse({'msg':'Record deleted successfully',})

@login_req
@csrf_exempt
def add_event(request,**kwargs):

	if request.method == "POST":
		event_form = EventForm(request.POST,request.FILES)

		if event_form.is_valid():

			event = event_form.save()
			event.save()

			return JsonResponse({
				'success' : True,
				'message' : 'Event added successfully'
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
def edit_event(request,pk,**kwargs):
	if request.method == 'POST':
		name = request.POST.get('name')
		detail = request.POST.get('details')
		cover_pic = request.FILES.get('cover_pic')
		email = request.POST.get('email')
		date = request.POST.get('date')
		venue = request.POST.get('venue')
		icon = request.FILES.get('icon')
		time = request.POST.get('time')
		try:
			event = Event.objects.get(pk=pk)
		except:
			return JsonResponse({
				'sucess':False,
				'message':'Record not found'
				})

		event.name = name
		event.details = detail
		event.cover_pic = cover_pic
		event.email = email
		event.date = date
		event.time = time
		event.venue = venue
		event.icon = icon
		#event.flag = flag
		event.save()
		events = model_to_dict(event, fields=['name', 'venue','details','date', 'time', 'email','flag'])

		events['cover_pic'] = str(event.cover_pic)
		events['icon'] = str(event.icon)
		return JsonResponse({
				'success':True,
				'Event': events,

		},safe=False)
	else:
		return JsonResponse({
			'sucess':False,
			'message':'Method Error'
})
