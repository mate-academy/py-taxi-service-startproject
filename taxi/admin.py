from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_display = ("model", "manufacturer")
    list_filter = ("manufacturer__name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {
                "classes": ("wide",),
                "fields": ("license_number",),
            },
        ),
    )
