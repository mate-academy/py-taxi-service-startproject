from django.contrib import admin
from taxi.models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin

# Register your models here.


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "country",
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "manufacturer",
    ]
    search_fields = [
        "model",
    ]
    list_filter = [
        "manufacturer",
    ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
