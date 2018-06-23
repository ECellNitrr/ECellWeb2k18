from django import forms
from .models import Answer

class AnswerForm(forms.ModelForm):
    answer = forms.IntegerField()
    class Meta():
        model = Answer
        fields = ('answer',)
