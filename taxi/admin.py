from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer

from taxi.models import Car

from taxi.models import Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model", "manufacturer__name"]
    list_display = ["model", "manufacturer"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number", )}),)