from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )
    list_display = ["username", "license_number", "email", "is_staff"]

