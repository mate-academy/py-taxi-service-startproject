from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    def display_drivers(self, obj):
        return ", ".join(driver.username for driver in obj.drivers.all())

    search_fields = ("model", )
    list_filter = ("manufacturer", )
    list_display = ("manufacturer", "model", "display_drivers")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields":
    ("license_number", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields":
    ("license_number", )}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")