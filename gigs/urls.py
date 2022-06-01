from django.urls import path
from . import views

app_name = 'gigs'

urlpatterns = [
    path(
        'home/',
         views.gig_view,
         name='home'
    ),
    path(
        'gigs/',
        views.ManageGigList.as_view(),
        name='gig-list'
    ),
    path(
        'gig/create/',
        views.GigCreateView.as_view(),
        name='gig-create'
    ),
    path(
        'gig/detail/<slug:slug>/',
        views.GigDetailView.as_view(),
        name='gig-detail'
    ),
]
