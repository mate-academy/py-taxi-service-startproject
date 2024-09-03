from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "get_manufacturer_name")
    list_filter = ("manufacturer", )
    search_fields = ("model", )

    def get_manufacturer_name(self, obj):
        return obj.manufacturer.name

    get_manufacturer_name.short_description = "Manufacturer"


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {
            "fields": (
                "license_number",
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": (
                "first_name",
                "last_name",
                "email",
                "license_number",
            )
        }),
    )
