# social_website/account/admin.py

from account.models import Contact, Profile
from django.contrib import admin


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']


admin.site.register(Contact)
