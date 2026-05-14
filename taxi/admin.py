from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "email", "first_name", "last_name", "license_number")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass