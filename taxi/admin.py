from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = *UserAdmin.fieldsets, (
        "Additional info",
        {"fields": ("license_number",)},
    )
    add_fieldsets = *UserAdmin.add_fieldsets, (
        "Additional info",
        {"fields": ("license_number",)},
    )
    list_display = (
        "username", "email", "license_number", "first_name", "last_name"
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model", )
    list_filter = ("manufacturer", )
