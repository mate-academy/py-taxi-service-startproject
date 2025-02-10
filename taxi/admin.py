from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "license_number")
    ordering = ["username",]
    search_fields = ("username", "license_number")
    fieldsets = UserAdmin.fieldsets + (
        ("Addition Info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Addition Info", {"fields": ("license_number",)}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model")
    search_fields = ("model",)
    list_filter = ("manufacturer",)
