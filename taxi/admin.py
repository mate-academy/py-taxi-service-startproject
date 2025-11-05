from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import *


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ["username", "license_number"]
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = (
        "manufacturer",
    )
