from django.contrib import admin

from taxi.models import Manufacturer, Driver, Car


# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "license_number", "first_name", "last_name")
    search_fields = ("username", "license_number")

    fieldsets = (
        ("Personal Information", {
            "fields": ("username", "email", "first_name", "last_name"),
        }),
        ("Additional info", {
            "fields": ("license_number",),
        }),
    )

    add_fieldsets = (
        ("Additional info", {
            "fields": ("license_number", "first_name", "last_name"),
        }),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("country",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model",)
    search_fields = ("model", "manufacturer")
