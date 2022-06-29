from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


class DriversInline(admin.TabularInline):
    model = Car.drivers.through
    extra = 1


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]
    list_display = ["model", "manufacturer", "enable_drivers"]
    inlines = (DriversInline,)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number", "enable_cars")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("licence_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("licence_number", "first_name", "last_name")}
        ),
    )
    inlines = (DriversInline,)
