from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("INFO", {"fields": ("license_number",)}),
    )
    list_display = UserAdmin.list_display + ("license_number",)
    list_filter = UserAdmin.list_filter + ("license_number",)
    search_fields = UserAdmin.search_fields + ("license_number",)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    list_filter = ("manufacturer", "model")
    search_fields = ("model",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
