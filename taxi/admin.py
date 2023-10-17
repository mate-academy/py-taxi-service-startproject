from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


# Register your models here.
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    search_fields = ("username", "license_number")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("country",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model",)
    search_fields = ("model",)
    list_filter = ("manufacturer",)
