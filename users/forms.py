from captcha import fields, widgets
from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UsernameField


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput())
    remember_me = forms.BooleanField(required=False)  # and add the remember_me field

