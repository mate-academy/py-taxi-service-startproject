from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class AdminDriver(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)
    ordering = ("model",)


@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    list_display = ("name", "country",)
    ordering = ("name",)
