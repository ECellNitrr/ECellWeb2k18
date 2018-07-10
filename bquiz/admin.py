from django.contrib import admin
from django.db import models
from .models import Questionset,Question,Answer

class QuestionsetAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'set_no','meta','flag')
    search_fields = ('id', 'name', 'description', 'set_no','meta','flag')
    list_filter = ('name',)

admin.site.register(Questionset, QuestionsetAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id','question', 'meta', 'description', 'time_limit','score','q_type','q_set','flag')
    search_fields = ('id','question', 'meta', 'description', 'time_limit','score','q_type','q_set','flag')
    list_filter = ('q_set',)

admin.site.register(Question, QuestionAdmin)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_id', 'user_id', 'answer')
    search_fields = ('id', 'question_id', 'user_id', 'answer')
    list_filter = ('question_id',)

admin.site.register(Answer, AnswerAdmin)
