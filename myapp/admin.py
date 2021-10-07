from django.contrib import admin as dj_admin
from django_neomodel import admin as neo_admin

from .models import Person, Address


class PersonAdmin(dj_admin.ModelAdmin):
    list_display = ("lastname", "firstname")


class AddressAdmin(dj_admin.ModelAdmin):
    list_display = ("city", )


neo_admin.register(Person, PersonAdmin)
neo_admin.register(Address, AddressAdmin)
