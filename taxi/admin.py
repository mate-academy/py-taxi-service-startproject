from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import *


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)

    add_fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)
    filter_horizontal = ("driver",)


# Register your models here.
