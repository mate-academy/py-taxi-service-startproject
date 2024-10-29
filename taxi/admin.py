from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info", {
                "fields": ("license_number",)
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info", {
                "fields": ("first_name", "last_name", "license_number",)
            }
        ),
    )
    search_fields = ["username", "first_name", "last_name", "license_number"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name"]
    list_filter = ["country"]
