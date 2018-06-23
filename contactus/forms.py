from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    subject = forms.CharField()
    message = forms.CharField()
    class Meta():
        model = Message
        fields = ('subject','message')
