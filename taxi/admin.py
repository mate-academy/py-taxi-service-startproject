from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "country")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": ("license_number",)}),
    )
    list_display = ("username", "first_name", "last_name", "license_number", "is_staff")
    search_fields = ("username", "license_number", "email")



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
