from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("license_number", "username", "email", "first_name", "last_name", )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_field_sets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country", )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "manufacturer",
        "model",
    )

    search_fields = ["model",]
    list_filter = ["manufacturer",]
