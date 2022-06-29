from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("License", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("License", {"fields": ("license_number",)}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]
