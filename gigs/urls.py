from django.urls import path
from gigs.views import (
    # GigListView,
    GigDetailView,
    )
from . import views

app_name = 'gigs'

urlpatterns = [
    path('gig_view/', views.gig_view, name='gig_view'),
    # path('', view=views.GigListView.as_view(), name='gig_list'),
    path('create/', views.create_gig, name='gig_create'),
    path('detail/<int:id>/<slug:slug>/',
         GigDetailView.as_view(), name='detail'),
]
