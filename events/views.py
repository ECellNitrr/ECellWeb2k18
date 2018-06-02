from django.shortcuts import render
from .models import Event
from django.http import JsonResponse
from server.decorators.login import login_req
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt#remove this , just an example of how to use this
@login_req #remove this , just an example of how to use this
def get_events(request):
    events= Event.objects.all().values()
    events_list=list(events)

    return JsonResponse({'Events':events_list}, safe=False)
