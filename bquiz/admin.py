from django.contrib import admin
from django.db import models
from .models import Questionset, Question, Answer, Option, Setting, QuestionAcknowledge,RightAnswer,Leader
from django.utils.translation import ugettext_lazy as _

class QuestionsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'set_no','meta','flag')
    search_fields = ('id', 'name', 'description', 'set_no','meta','flag')
    list_filter = ('name',)

admin.site.register(Questionset, QuestionsetAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'user', 'option')
    search_fields = ('id', 'question', 'user', 'option')
    list_filter = ('question',)

admin.site.register(Answer, AnswerAdmin)

class RightAnswerAdmin(admin.ModelAdmin):
    list_display = ('question','right_option')
    search_display = ('question','right_option')
    list_filter = ('question',)

admin.site.register(RightAnswer,RightAnswerAdmin)


class LeaderAdmin(admin.ModelAdmin):
    list_display = ('questionset','profile','score')
    search_display = ('questionset','profile','score')
    list_filter = ('questionset',)

admin.site.register(Leader,LeaderAdmin)

class OptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'option', 'question')
    search_fields = ('id', 'option', 'question')
    list_filter = ('question',)

admin.site.register(Option, OptionAdmin)

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

class QuestionAcknowledgeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'question')
    
admin.site.register(QuestionAcknowledge, QuestionAcknowledgeAdmin)