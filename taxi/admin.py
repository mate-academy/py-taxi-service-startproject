from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", ]
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
    search_fields = ["name", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "license_number",
    )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number",)}
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number",)}
        ),
    )
