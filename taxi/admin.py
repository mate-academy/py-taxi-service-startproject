from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]
    fieldsets = [
        ("Car", {"fields": ["model", "manufacturer"]}),
        ("Drivers", {"fields": ["drivers"]})
    ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
