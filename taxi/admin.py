from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    fields = ["model", "manufacturer", "drivers"]
    list_filter = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "email", "license_number", "is_staff")
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


admin.site.register(Manufacturer)
