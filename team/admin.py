from django.contrib import admin

from django.db import models
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'member_type')
    search_fields = ('id', 'name', 'member_type')
    list_filter = ('member_type',)
   

admin.site.register(Member, MemberAdmin)