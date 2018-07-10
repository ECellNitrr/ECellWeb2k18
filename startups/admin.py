from django.contrib import admin
from django.db import models
from .models import Startup

class StartupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founder', 'contact','email')
    search_fields = ('id', 'name', 'founder', 'contact','email')
   # list_filter = ('spons_type',)
    #ordering = ('-created_at',)
    #readonly_fields = ('created_at', 'modified_at')

admin.site.register(Startup, StartupAdmin)