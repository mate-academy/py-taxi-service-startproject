from django.contrib import admin

from taxi.models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin

admin.site.register(Manufacturer)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", "driver", ]
    search_fields = ["model"]
    list_filter = ["manufacturer"]

    @staticmethod
    def driver(other: type) -> str:
        return "\n".join([
            owner.username for owner in other.drivers.all()
        ])


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + ((
        "Additional info",
        {"fields": ("license_number", )}
                                             ), )
    add_fieldsets = UserAdmin.add_fieldsets + ((
        "Additional info",
        {"fields": ("license_number", )}
                                             ), )
