from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "drivers_list")
    list_filter = ("manufacturer",)
    search_fields = ("model",)

    def drivers_list(self, obj):
        return "\n".join(
            [f"{driver.first_name} {driver.last_name}"
            for driver in obj.drivers.all()]
        )


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number", "first_name", "last_name")}), )


admin.site.register(Manufacturer)
