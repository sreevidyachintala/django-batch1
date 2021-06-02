from django import forms

from app1.models import Register


class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register

		fields = '__all__'

		widgets={

		'name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter your name'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'example@gmail.com'}),
		'age':forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your age'}),
		'mobile_no':forms.TextInput(attrs={'class':'form-control','placeholder':'enter your mobile number'})


		}