from django.contrib import admin

<<<<<<< HEAD
# Register your models here.
=======
from django.db import models
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'member_type')
    search_fields = ('id', 'name', 'member_type')
    list_filter = ('member_type',)
   

admin.site.register(Member, MemberAdmin)
>>>>>>> 81cdb9c8421ab187806be8f969045707294e7b34
