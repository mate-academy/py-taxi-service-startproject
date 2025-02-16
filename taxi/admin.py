from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")

@admin.register(Driver)
class DriverAdmin(UserAdmin):  # Extends UserAdmin for authentication
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),  # Custom category for editing
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),  # Custom category for adding
    )
    list_display = ("username", "email", "first_name", "last_name", "license_number", "is_staff", "is_active")
    search_fields = ("username", "email", "license_number")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)  # Allows searching by model
    list_filter = ("manufacturer",)  # Enables filtering by manufacturer
    filter_horizontal = ("drivers",)  # Better UI for ManyToMany fields
