from django import forms
from django.forms import ModelForm
from .models import Login



class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields= ['name', 'email', 'password']