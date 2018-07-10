from django import forms
from .models import Sponsor

class SponsorForm(forms.ModelForm):
    SPONS_TYPE = (
        ('AS', 'Associate Sponsors'),
        ('PLTS', 'Platinum Sponsors'),
        ('GS', 'Gold Sponsors'),
        ('TS', 'Title Sponsors'),
        ('PRTS', 'Partner Sponsors'),

    )
    name = forms.CharField(max_length=256)
    details = forms.CharField()
    pic = forms.ImageField()
    contact = forms.CharField()
    website = forms.URLField()
    spons_type = forms.CharField()
    class Meta():
        model = Sponsor
        fields = ('name','details', 'contact', 'website','spons_type')
