from django.urls import path
from gigs.views import (
    GigListView,
    GigDetailView,
    )
from . import views

app_name = 'images'

urlpatterns = [
    path('gigs/', GigListView.as_view()),
    path('create/', views.create_gig, name='name'),
    path('detail/<int:id>/<slug:slug>/',
         GigDetailView.as_view(), name='detail'),
]
