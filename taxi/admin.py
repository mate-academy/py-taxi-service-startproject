from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Licence", {"fields": ("licence_number",)},),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Personal information", {
        "fields": ("first_name", "last_name", "email", "licence_number",)},),)
