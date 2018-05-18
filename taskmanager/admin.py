from django.contrib import admin
from django.db import models
from django.forms import Textarea
from django.utils.translation import ugettext_lazy as _
from .models import Task, CheckList


class ItemInline(admin.TabularInline):
    model = CheckList
    extra = 0


class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'assigned_to', 'created_at', 'deadline', 'priority', 'state')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'item__description',
                     'assigned_to__user', 'assigned_to__user__first_name', 'assigned_to__user__last_name')
    list_filter = ('state', 'priority', 'deadline')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'modified_at')

    # Edition form
    fieldsets = (
        ( None , {
            'fields': ('title', ('assigned_to', 'deadline'), ('state', 'priority'), ('description'))
        }),
        (_('More...'), {
            'fields': (('created_at', 'modified_at'), 'assigned_by'), 
            'classes': ('collapse',)
        }),
    )
    inlines = [ItemInline]

    formfield_overrides = {
        models.TextField: {
            'widget': Textarea(attrs={'rows': 4, 'cols': 32})
        }
    }

    def get_fieldsets(self, request, obj=None):
        fieldsets = super().get_fieldsets(request, obj)
        if obj is None:
            fieldsets = (      # Creation form
                (None, {'fields': ('title', ('assigned_to', 'deadline'), ('state', 'priority'), 'description')}),
            )
        return fieldsets

    def save_model(self, request, obj, form, change):
        if change is False:
            obj.assigned_by = request.user.profile
        super().save_model(request, obj, form, change)


admin.site.register(Task, TaskAdmin)