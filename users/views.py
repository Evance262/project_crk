#!/usr/bin/python3
"""
Login view to provide login functionality
using the Django authentication framework
Performamces:
    1: Get username & password
    2: Authenticate user
"""
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm


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
                    return redirect('dashboard')
                else:
                    messages.info(request, 'Disabled account')
            else:
                messages.info(request, 'Username or password is incorrect')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})


def logoutUser(request):
    """
    Redirects to a success page
    """
    logout(request)
    return render('login')


def register(request):
    """Creating a new user account.
       set_password: A password hashing method for security"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the user object
            new_user.save()

            return render(request,
                          'users/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
        
    return render(request,
                  'users/register.html',
                  {'user_form': user_form})


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


@login_required
def dashboard(request):
    return render(request,
                  'users/dashboard.html',
                  {'section': 'dashboard'})