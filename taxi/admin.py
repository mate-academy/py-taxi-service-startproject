from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "get_drivers")
    list_filter = ("manufacturer", )
    search_fields = ("model", )

    def get_drivers(self, obj) -> str:
        return ", ".join(driver.username for driver in obj.drivers.all())

    get_drivers.short_description = "drivers"


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number", )}
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number", )}
        ),
    )
