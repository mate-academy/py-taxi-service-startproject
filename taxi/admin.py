from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


class DriversInline(admin.TabularInline):
    model = Car.drivers.through


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "license_number",
                )
            }
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "fields": (
                    "license_number",
                )
            }
        ),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "get_drivers")
    search_fields = ("model",)
    list_filter = ("manufacturer",)

    @admin.display(
        empty_value="No drivers",
        description="Drivers"
    )
    def get_drivers(self, obj):
        return ", ".join(obj.drivers.values_list("username", flat=True))
