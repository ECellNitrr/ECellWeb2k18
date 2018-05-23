from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
	email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}))
	class Meta():
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'First Name'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Last Name'}))
	contact_no = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Contact No'}))
	#college = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'College Name'}))
	#dob = forms.DateField(widget=forms.SelectDateWidget(years=[y for y in range(1930,2050)],attrs={'class':'form-control form-inline inline inlinef'}))
	#doc_image = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Document Image'}))
	avatar = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','placeholder':'Profile Pic'}))
	linkedin = forms.CharField(widget=forms.TextInput())
	facebook = forms.CharField(widget=forms.TextInput())
	class Meta():
		model= Profile
		fields = ('first_name','last_name','contact_no','facebook','linkedin','avatar')
