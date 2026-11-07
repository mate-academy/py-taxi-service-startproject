from django.contrib import admin

from taxi.models import Driver, Manufacturer, Car
from django.contrib.auth.admin import UserAdmin


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        "Additional info",
        {"fields": ("username", "license_number")},
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", "drivers__username"]

    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
