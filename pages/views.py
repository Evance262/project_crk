from django.shortcuts import render
from django.views.generic import TemplateView


class LandingPage(TemplateView):
    template_name = 'landing_page.html'

class HomePage(TemplateView):
    template_name = 'home.html'


class ContactPage(TemplateView):
    template_name = 'contact.html'