from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["username", "license_number"]
    fieldsets = UserAdmin.fieldsets + (
        (("Additional info"), {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model", "manufacturer__name"]
