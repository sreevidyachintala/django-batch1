from django import forms
from django.forms import ModelForm

from dtlapp.models import update

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserReg(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	class Meta:
		model  = User
		fields = ['username','email']

		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Eneter your username'}),
		'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Example@gmail.com'}),
			}

class Uppro(ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email']
		widgets={
		'username':forms.TextInput(attrs={'class':'form-control','placeholder':'enter username'}),
		'first_name':forms.TextInput(attrs={
			'class':'form-control','placeholder':'enter first_name'
			}),
		'last_name':forms.TextInput(attrs={
			'placeholder':'enter your last_name','class':'form-control'
			}),
		'email':forms.EmailInput(attrs={
			'placeholder':'enter your email','class':'form-control'
			})
		}
	
class imagepro(forms.ModelForm):
	class Meta:
		model = update
		fields=['image','age']
		widgets={
		'age':forms.NumberInput(attrs={'class':'form-control'})
				}