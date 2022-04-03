from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['name', 'country']
    search_fields = ['name', 'country']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ['manufacturer']
    list_display = ['manufacturer', 'model']
    search_fields = ['manufacturer', 'model']


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info", {"fields": ("first_name", "last_name",)}),
        ("Additional info", {"fields": ("license_number",)}),
    )
