from django.shortcuts import render

# Create your views here.
from .models import Event
from django.http import JsonResponse

def get_mentors(request):
    events= Event.objects.all().values()
    events_list=list(events)

    return JsonResponse(events_list, safe=False)

