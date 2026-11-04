from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name", "country")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    search_fields = ("license_number", "username", "email", "password", "first_name", "last_name")
    list_display = ("license_number",)
    fieldsets = ("Additional Info",)
    add_fieldsets = ("Additional Info",)