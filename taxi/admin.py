from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin:
    list_display = ["name", "country"]


@admin.register(Car)
class CarAdmin:
    list_display = ["model", "manufacturer", "drivers"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (("Additional info", {"fields": ("license_number",)}),)
    )
