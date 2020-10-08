from django import forms
from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
from app_drivers.models import *

# class UserRegisterForm(UserCreationForm):
# 	email = forms.EmailField(required=True)
# 	field_order = ['username', 'email', 'password1', 'password2']

# class ProfileCreationForm(forms.ModelForm):
# 	class Meta:
# 		model = UserProfile
# 		fields = ['customer']

class SignUpForm(UserCreationForm):
	REGIST_CUSTOMER = 'RC'
	REGIST_COMPANY_DRIVER = 'RCD'
#	REGIST_DRIVER = 'RD'

	CHOICE_REGISTER = [
		(REGIST_CUSTOMER, 'Организация производитель'),
		(REGIST_COMPANY_DRIVER, 'Организация перевозчик'),
#		(REGIST_DRIVER, 'Частный перевозчик')
	]


	email = forms.EmailField(required=True)
	name = forms.CharField(max_length=200)
	customer = forms.CharField(widget=forms.Select(choices=CHOICE_REGISTER))
	
	class Meta:
		model = User
		fields = ('username', 'name', 'customer', 'email', 'password1', 'password2', )	

# class OplataForm(forms.ModelForm):
# 	class Meta:
# 		model = Oplata
# 		fields= '__all__'