#!/usr/bin/python3
"""
URL patterns for the views
"""
from  django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth import urls
from . import views


urlpatterns = [
    # POST views
    path('login/', views.user_login, name='login'),
    path('users/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    # change password urls
    path('password_change/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         auth_views.PasswordChangeView.as_view(),
         name='password_change_done'),
]
