from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
    list_filter = ["name", ]
    search_fields = ["name", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ModelAdmin.list_display + ("license_number",)
    fieldsets = (UserAdmin.fieldsets +
                 (("Additional info", {"fields": ("license_number",)}),))
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Additional info", {"fields": ("license_number",)}),))


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model", ]
    list_filter = ["manufacturer", ]
