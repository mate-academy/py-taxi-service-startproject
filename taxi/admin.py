from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer

@admin.register(Driver)
class AdminDriver(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("first_name", "last_name", "license_number")}),
    )
    list_filter = ("first_name", "last_name", "license_number", "username")
    search_fields = ("first_name", "last_name", "license_number", "username")

@admin.register(Car)
class AdminCAr(admin.ModelAdmin):
    list_filter = ("model",)
    search_fields = ("manufacturer",)

@admin.register(Manufacturer)
class AdminManufacture(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name", "county")
    list_filter = ("name", "country")
