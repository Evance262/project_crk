#!/usr/bin/python3
"""
Login view to provide login functionality
using the Django authentication framework
Performamces:
    1: Get username & password
    2: Authenticate user
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Instantiating a new login form from GET method
def user_login(request):
    '''
        Instantiating form with the submetted data
        to desplay it in a template
    '''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


class PasswordChangeView:
    '''Allows a user to change their password.'''
    pass

class PasswordChangeDoneView:
    '''
        The page shown after a user
        has changed their password.'''
    pass


class PasswordResetView:
    """Generating a one-time use link that can
    be used to reset the password, and sending
    that link to the users registered email address."""
    pass