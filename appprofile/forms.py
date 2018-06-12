from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.CharField()
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	class Meta():
		model = User
		fields = ('first_name','last_name','username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	contact_no = forms.CharField(required=False)
	avatar = forms.ImageField(required=False)
	linkedin = forms.CharField(required=False)
	facebook = forms.CharField(required=False)
	class Meta():
		model= Profile
		fields = ('contact_no','facebook','linkedin','avatar')

class ContactForm(forms.ModelForm):
	contact_no = forms.CharField()
	class Meta():
		model = Profile
		fields = ('contact_no',)