from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "get_drivers")
    search_fields = ("model",)
    list_filter = ("manufacturer",)

    def get_drivers(self, obj):
        return ", ".join(
            f"{driver.first_name} {driver.last_name}"
            for driver in obj.drivers.all()
        )


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        "license_number",
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "is_superuser",
        "is_active"
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)
