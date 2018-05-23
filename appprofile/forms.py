from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
	username = forms.CharField()
	password = forms.CharField()
	email = forms.CharField()
	first_name = forms.CharField()
	last_name = forms.CharField()
	class Meta():
		model = User
		fields = ('first_name','last_name','username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	contact_no = forms.CharField()
	avatar = forms.ImageField()
	linkedin = forms.CharField()
	facebook = forms.CharField()
	class Meta():
		model= Profile
		fields = ('contact_no','facebook','linkedin','avatar')
