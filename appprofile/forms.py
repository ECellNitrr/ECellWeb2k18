from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserForm(forms.ModelForm):
	username = forms.CharField(required=False)
	password = forms.CharField()
	email = forms.CharField()
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	class Meta():
		model = User
		fields = ('first_name','last_name','email', 'password')
	def clean_email(self):
		email = self.cleaned_data.get('email')
		#username = self.cleaned_data.get('username')
		if email and User.objects.filter(email=email).exists():
			raise forms.ValidationError(u'Email addresses must be unique')
		return email

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
