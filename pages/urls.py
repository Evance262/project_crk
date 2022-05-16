from django.urls import path
from .views import ContactPage, LandingPage, HomePage

app_name = 'pages'

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('home/', HomePage.as_view(), name='home'),
    path('contact/', ContactPage.as_view(), name='contact'),
]
