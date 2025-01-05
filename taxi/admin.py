from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["license_number", "username", "email", "first_name", "last_name"]
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    search_fields = ["model", ]
    list_filter = ["manufacturer", ]
