from django.contrib import admin
from django.db import models
from .models import Speaker

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'company', 'email','contact')
    search_fields = ('id', 'name', 'company','email','contact')
    #list_filter = ('user_type',)
    ##readonly_fields = ('created_at', 'modified_at')

admin.site.register(Speaker, SpeakerAdmin)
