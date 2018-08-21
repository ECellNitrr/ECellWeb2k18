from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'venue', 'date','time')
    search_fields = ('id', 'name','venue','date', 'time')

admin.site.register(Event, EventAdmin)
