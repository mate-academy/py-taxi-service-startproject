from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from taxi.models import *


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["drivers", "model"]
    search_fields = ["model"]
    list_filter = ["-manufacturer"]


class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = UserAdmin.list_display + ("license_number",)


admin.site.register(Driver, DriverAdmin)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')