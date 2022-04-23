#!/usr/bin/python3
"""
Form to provide login functionality
using the Django authentication framework
Performamces:
    1: Get username & password
    2: Authenticate user
"""

from django import forms


class LoginForm(forms.Form):
    '''Authenticating users against the database'''
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
