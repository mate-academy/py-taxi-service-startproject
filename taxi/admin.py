from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Manufacturer, Car, Driver

# Register your models here.

# 1. Register Manufacturer normally
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)


# 2. Customize DriverAdmin to include license_number in fieldsets and list display
@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)

    # Add license_number to the fieldsets when editing an existing driver
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Add license_number to the add_fieldsets when creating a new driver
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


# 3. Customize CarAdmin to add search and filtering options
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)  # Make it possible to search Car by model
    list_filter = ("manufacturer",)  # Make it possible to filter Car by manufacturer