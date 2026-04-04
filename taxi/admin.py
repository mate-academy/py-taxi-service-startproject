from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, Driver, Manufacturer

# Register your models here.

admin.site.register(Manufacturer)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer",)
    search_fields = ("model",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "license_number")
    search_fields = ("username", "first_name", "last_name", "license_number")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
