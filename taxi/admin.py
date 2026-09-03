from django.contrib import admin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "license_number")
    fieldsets = (
        (None, {"fields": ("username",)}),
        (
            "Additional info",
            {
                "fields": ("license_number",),
            },
        ),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("username",)}),
        (
            "Additional info",
            {
                "fields": ("license_number",),
            },
        ),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "model")

    search_fields = ("model",)

    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
