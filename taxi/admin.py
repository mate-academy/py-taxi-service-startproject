from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer
from taxi.models import Car
from taxi.models import Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "license_number",
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer__country",)
    search_fields = ("model",)
    list_display = (
        "manufacturer",
        "model",
        "drivers",
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
    )
