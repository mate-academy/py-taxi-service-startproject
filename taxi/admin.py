from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import *


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email", "license_number")
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}), )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model", )
    list_display = ("model", "manufacturer", )
    list_filter = ("manufacturer", )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name", )
    list_display = ("name", "country", )
