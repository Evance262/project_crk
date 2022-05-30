from django.shortcuts import render
from django.views.generic import TemplateView
from . import views
from gigs.models import Gig


class LandingPage(TemplateView):
    template_name = 'landing.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'