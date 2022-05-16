from django.urls import path
from . import views

app_name = 'images'

urlpatterns = [
    path('create/', views.create_gig, name='name'),
    path('detail/<int:id>/<slug:slug>/',
         views.gig_detail, name='detail'),
]
