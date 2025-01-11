from django.contrib import admin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    # Display all fields including license_number
    list_display = ("id", "first_name", "last_name", "license_number")

    # Add license_number under 'Additional info' in fieldsets
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                )
            },
        ),
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Add license_number under 'Additional info' in add_fieldsets
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Add search functionality by model
    search_fields = ("model",)

    # Add filtering functionality by manufacturer
    list_filter = ("manufacturer",)
