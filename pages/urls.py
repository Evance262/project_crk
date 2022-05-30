from django.urls import path
from .views import ContactPage, LandingPage
from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
