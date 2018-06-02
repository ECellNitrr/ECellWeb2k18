from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    name = forms.CharField(max_length=256)
    venue = forms.CharField()
    details = forms.CharField()
    cover_pic = forms.ImageField()
    icon = forms.ImageField()
    email = forms.EmailField()
    date = forms.DateField()
    time = forms.CharField()

    class Meta():
        model = Event
        fields = ('name','venue', 'details', 'cover_pic', 'icon','email','date','time')
