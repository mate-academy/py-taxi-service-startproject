from django.contrib import admin
from taxi.models import Manufacturer
from taxi.models import Car
from taxi.models import Driver
from django.contrib.auth.admin import UserAdmin


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["model"]
    search_fields = ["manufacturer"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info",
                                        {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.fieldsets + (("Additional info",
                                            {"fields": ("license_number",)}),)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
