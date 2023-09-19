from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi_service.taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = [
        "license_number",
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ["license_number"]}),
    )

    add_fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ["license_number"]}),
    )
