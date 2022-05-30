from django.urls import path
from gigs.views import (
    GigDetailView,
    )
from . import views

app_name = 'gigs'

urlpatterns = [
    path('home/', views.gig_view, name='home'),
    path('create/', views.create_gig, name='gig-create'),
    path('gig/detail/<slug:slug>/',
         views.GigDetailView.as_view(), name='gig-detail'),
]
