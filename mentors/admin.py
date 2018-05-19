from django.contrib import admin
from django.db import models
from .models import Mentor 
class MentorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'contact')
    search_fields = ('id', 'name','email', 'contact')
   # list_filter = ('user_type',)
    #ordering = ('-created_at',)
    #readonly_fields = ('created_at', 'modified_at')

admin.site.register(Mentor, MentorAdmin)