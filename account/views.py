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
from django.contrib.auth import (
    get_user_model,
    authenticate,
    login,
    logout,
)
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UserRegistrationForm, \
                   UserEditForm, ProfileEditForm
from .models import Profile

from django.views.generic import (
    DetailView,
    RedirectView,
    UpdateView
)


User = get_user_model()


# Instantiating a new login form from GET method
def user_login(request):
    '''
        Instantiating form with the submetted data
        to desplay it in a template
    '''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # cd = form.cleaned_data
            user = authenticate(request,
                                username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Disabled account')
            else:
                messages.error(request, 'Username or password is incorrect')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def logoutUser(request):
    """
    Redirects to a success page
    """
    logout(request)
    return render('account:login')


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
            # create the profile
            Profile.objects.create(user=new_user)

            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    return render(request,
                  'account/register.html',
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
                  'account/dashboard.html',
                  {'section': 'dashboard'})


@login_required
def edit(request):
    """
    UserEditForm: tores the data of the built-in user model
    ProfileEditForm: Stores the additional profile data in 
                     the custom profile model
    """
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_for.save()
            profile_form.save()
            messages.success(request, 'Profile updated '\
                                      'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                       instance=request.user)

    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                  'profile_form': profile_form})
