from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number", )}), )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number", )}), )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country", )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model", )
    search_fields = ("model", )
    list_filter = ("manufacturer",)
