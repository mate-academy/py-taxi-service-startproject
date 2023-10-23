from django.contrib import admin
from taxi.models import Manufacturer, Driver, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "license_number",
        "username",
        "email",
        "first_name",
        "last_name"
    )
    fieldsets = (
        (None, {
            'fields': ("username", "email", "first_name", "last_name")
        }),
        ("Additional info", {
            'classes': ("collapse",),
            'fields': ("license_number",),
        }),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


