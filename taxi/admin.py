from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer__name", ]

    # own initiative
    # list_display = ["model", "manufacturer", "get_drivers"]
    #
    # def get_drivers(self, obj):
    #     return ", ".join(driver.username for driver in obj.drivers.all())
    #
    # get_drivers.short_description = "Drivers"


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
    # own initiative
    # list_display = ["name", "country",]
    # list_filter = ["name",]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info: ", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info: ",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "license_number",
                )
            },
        ),
    )
