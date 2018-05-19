from django.contrib import admin
from django.db import models
from .models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subject', 'message')
    search_fields = ('id', 'name', 'subject', 'message')

admin.site.register(Message, MessageAdmin)
