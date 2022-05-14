from django.contrib import admin
from account.models import Passport, Identity
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseAdmin
# from .forms import UserCreationForm

from django.contrib.auth import get_user_model

User = get_user_model()


class IdentityInline(admin.StackedInline):
    model = Identity
    extra = 1

class PassportInline(admin.StackedInline):
    model = Passport
    extra = 1


class UserAdmin(BaseAdmin):
    list_display = ['username', 'first_name', 'last_name', 'gender', 'is_buyer', 'is_seller']
    inlines = [IdentityInline, PassportInline]
    search_fields = ['username', 'first_name', 'last_name']
    ordering = ('gender',)
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'gender', 'date_of_birth', 
            'password1', 'password2', 'image', 'address')
        }),
        ('permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )
    fieldsets = (
        (None, {
                'fields': ('username', 'first_name', 'last_name', 'is_buyer', 'is_seller', 'password')
        }),
        ('permissions', {
            'fields': ('is_superuser', 'is_staff')
        })
    )


admin.site.register(User, UserAdmin)