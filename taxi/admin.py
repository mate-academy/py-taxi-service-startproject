from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Show license number in the list
    list_display = ("username", "email", "first_name", "last_name", "license_number", "is_staff")

    # Add license_number to search
    search_fields = ("username", "email", "first_name", "last_name", "license_number")

    # Add license number to fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Add license number to add_fieldsets (for creating new users)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


# --- Car ADMIN ---

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)  # Search by model
    list_filter = ("manufacturer",)  # Filter by manufacturer


# --- Manufacturer ADMIN ---

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")
