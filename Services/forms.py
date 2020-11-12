
from django.forms import ModelForm
from django import forms
from Services.models import Tiling_Services,Plumbing_Services

class service_installer (forms.Form) :
    Name = forms.CharField(
        max_length=16,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Your Name",
                "class":"form-control"
            }
        )
    )
    Contact = forms.CharField(
        max_length=13,
        widget=forms.TextInput(
            attrs={
                "placeholder":"Your contact please",
                "class":"form-control"
            }
        )
    )
    Email = forms.EmailField(
        max_length=20,
        widget=forms.EmailInput(
            attrs={
                "placeholder":"Email",
                "class":"form-control"
            }
        )
    )
    Password = forms.CharField(
        max_length=10,
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Password",
                "class":"form-control",
            }
        )
    )
    profile_pic = forms.ImageField()
    

    

class login_view_form (forms.Form):
    Name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder":"Your name please",
                "class":"form-control",
            }
        )
    )
    Password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder":"Your password",
                "class":"form-control"
            }
        )
    )
   

