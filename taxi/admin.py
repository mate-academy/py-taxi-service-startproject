from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["pk", "name", "country"]
    list_display_links = ["name"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["pk", "model", "manufacturer"]
    list_filter = ["manufacturer__name"]
    search_fields = ["model"]
    list_display_links = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
