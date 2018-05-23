from django.contrib import admin
from .models import Event

# Register your models here.
class EventAdmin(adminEventAdmin):
    list_display = ('id', 'name', 'venue', 'date','time')
    search_fields = ('id', 'name','venue','date', 'time')
   # list_filter = ('user_type',)
    #ordering = ('-created_at',)
    #readonly_fields = ('created_at', 'modified_at')

admin.site.register(Event, EventAdmin)