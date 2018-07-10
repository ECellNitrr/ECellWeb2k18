from django.contrib import admin
from django.db import models
from .models import Sponsor

class SponsorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'spons_type', 'contact','website')
    search_fields = ('id', 'name', 'spons_type', 'contact','website')
    list_filter = ('spons_type',)
    #ordering = ('-created_at',)
    #readonly_fields = ('created_at', 'modified_at')

admin.site.register(Sponsor, SponsorAdmin)