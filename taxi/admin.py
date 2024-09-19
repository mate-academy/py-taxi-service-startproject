from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = [
        "username",
        "email",
        "password",
        "first_name",
        "last_name",
        "license_number",
    ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
