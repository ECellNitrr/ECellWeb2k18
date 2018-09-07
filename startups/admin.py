from django.contrib import admin
from django.db import models
from .models import Startup, StartupRegister

class StartupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'founder', 'contact','email')
    search_fields = ('id', 'name', 'founder', 'contact','email')
   # list_filter = ('spons_type',)
    #ordering = ('-created_at',)
    #readonly_fields = ('created_at', 'modified_at')

class StartupRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'startup')
    search_fields = ('id', 'profile', 'startup')



admin.site.register(Startup, StartupAdmin)
admin.site.register(StartupRegister, StartupRegisterAdmin)





