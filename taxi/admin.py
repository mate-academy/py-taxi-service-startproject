from django.contrib import admin
from .models import Car, Manufacturer, Driver


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["username", "email", "first_name", "last_name", "license_number"]
    fieldsets = (
        (None, {
            "fields": ("username", "email", "first_name", "last_name", "password")
        }),
        ("Additional info", {
            "classes": ("collapse",),
            "fields": ("license_number",),
        }),
    )
    add_fieldsets = (
        (None, {
            "fields": ("username", "email", "first_name", "last_name", "password")
        }),
        ("Additional info", {
            "classes": ("collapse",),
            "fields": ("license_number",),
        }),
    )
    list_filter = ["license_number"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer", "drivers"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
