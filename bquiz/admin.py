from django.contrib import admin
from django.db import models
from .models import Questionset, Question, Answer, Option, Setting, QuestionAcknowledge
from django.utils.translation import ugettext_lazy as _

class QuestionsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'set_no','meta','flag')
    search_fields = ('id', 'name', 'description', 'set_no','meta','flag')
    list_filter = ('name',)

admin.site.register(Questionset, QuestionsetAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_id', 'user_id', 'answer')
    search_fields = ('id', 'question_id', 'user_id', 'answer')
    list_filter = ('question_id',)

admin.site.register(Answer, AnswerAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option', 'question')
    search_fields = ('id', 'option', 'question')
    list_filter = ('question',)

admin.site.register(Option, OptionAdmin)

class QuestionAcknowledgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question')

admin.site.register(QuestionAcknowledge, QuestionAcknowledgeAdmin)

class SettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'text')
    list_filter = ('key',)

admin.site.register(Setting, SettingAdmin)

class ItemInline(admin.TabularInline):
    model = Option
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'meta', 'description', 'time_limit','score','type','set','flag')
    search_fields = ('id','question', 'meta', 'description', 'time_limit','score','type','set','flag')
    list_filter = ('set',)
    readonly_fields = ('created_at', 'modified_at')
    ordering = ('-created_at',)

    fieldsets = (
        ( None , {
            'fields': ('question', ('set', 'flag'), ('description'), ('type', 'meta'), ('time_limit', 'score'), )
        }),
        (_('More...'), {
            'fields': (('created_at', 'modified_at'),), 
            'classes': ('collapse',)
        }),
    )

    inlines = [ItemInline]

admin.site.register(Question, QuestionAdmin)