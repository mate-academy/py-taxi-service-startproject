from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Displays license_number in the driver list view alongside standard fields
    list_display = UserAdmin.list_display + ("license_number",)

    # Adds license_number to the editing form
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Adds license_number to the creation form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Enables searching cars by model name
    search_fields = ["model"]

    # Enables filtering cars by manufacturer
    list_filter = ["manufacturer"]


# Register Manufacturer with default configuration
admin.site.register(Manufacturer)
