#!/usr/bin/python3
"""
Form to provide login functionality
using the Django authentication framework
Performamces:
    1: Get username & password
    2: Authenticate user
"""

from django import forms
from .models import User


class LoginForm(forms.Form):
    '''Authenticating users against the database'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Mmmmh looks like the passwords don\'t match.')
        return cd['password2']