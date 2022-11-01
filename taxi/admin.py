from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "licence_number")


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]
