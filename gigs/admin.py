from django.contrib import admin
from .models import Gig

@admin.register(Gig)
class GigAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created']
    list_filter = ['created']