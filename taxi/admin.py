from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class TaxiAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", "display_drivers"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]

    def display_drivers(self, obj):
        return ", ".join([driver.username for driver in obj.drivers.all()])

    display_drivers.short_description = "Drivers"
