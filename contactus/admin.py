from django.contrib import admin
from django.db import models
from .models import Message
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'message')
    search_fields = ('id', 'user', 'subject', 'message')

admin.site.register(Message, MessageAdmin)
