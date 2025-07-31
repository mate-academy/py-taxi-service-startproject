from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + (
        "first_name",
        "last_name",
        "license_number",
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "license_number",
                )
            },
        ),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model", "get_drivers")
    search_fields = ("model",)
    list_filter = ("manufacturer",)

    def get_drivers(self, obj):
        return ", ".join(
            [
                f"{driver.first_name} {driver.last_name} {driver.license_number}"
                for driver in obj.drivers.all()
            ]
        )

    get_drivers.short_description = "Drivers"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
