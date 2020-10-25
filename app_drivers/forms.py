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
	PRIVITE_DRIVER = 'PD'
#	REGIST_DRIVER = 'RD'

	CHOICE_REGISTER = [
		(REGIST_CUSTOMER, 'Организация производитель'),
		(REGIST_COMPANY_DRIVER, 'Организация перевозчик'),
		(PRIVITE_DRIVER, 'Частный перевозчик',)
#		(REGIST_DRIVER, 'Частный перевозчик')
	]

	IP = 'IP'
	OOO = 'OOO'
	PD = 'Частный перевозчик'

	TYPE_ORGANIZATION = [
		(IP, 'ИП',),
		(OOO, 'ООО'),
		(PD, 'Частный перевозчик')
	]

	email = forms.EmailField(required=True)
	name = forms.CharField(max_length=200, label='Наименование организации', help_text='<em>Например: "OOO Винтрест"</em>' )
	type_organization = forms.CharField(widget=forms.Select(choices=TYPE_ORGANIZATION), label='Тип деятельности')
	customer = forms.CharField(widget=forms.Select(choices=CHOICE_REGISTER), label='Вид деятильности')
	
	class Meta:
		model = User
		fields = ('username', 'name', 'type_organization', 'customer', 'email', 'password1', 'password2', )	

# class OplataForm(forms.ModelForm):
# 	class Meta:
# 		model = Oplata
# 		fields= '__all__'