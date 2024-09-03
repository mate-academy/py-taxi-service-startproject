from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ["username", "first_name", "last_name", "email", "license_number", ]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "email", "license_number", )}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", ]
    search_fields = ["model", ]
    list_filter = ["manufacturer", ]
