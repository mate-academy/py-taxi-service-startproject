from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Car, Manufacturer


# Register your models here.


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "license_number", "first_name", "last_name")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
