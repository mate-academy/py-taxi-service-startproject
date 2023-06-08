from django.contrib import admin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = (
        "model",
        "manufacturer",
    )
    search_field = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("license_number", "username", "email", "first_name", "last_name")
    fieldsets = (
        (
            None,
            {"fields": ("username", "email", "password", "first_name", "last_name")},
        ),
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "email",
                    "license_number",
                ),
            },
        ),
    )
