from django.contrib import admin

# Register your models here.
from .models import Member

class TeamAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'image', 'profile_url', 'member_type')
    search_fields = ('id', 'name', 'image', 'profile_url', 'member_type')

admin.site.register(Member, TeamAdmin)