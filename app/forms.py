from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    class Meta:
        model = User   
        fields =["username","password1","password2",'email']
    username = forms.CharField()
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput())
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput())
    email = forms.EmailField()


class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields = "__all__"