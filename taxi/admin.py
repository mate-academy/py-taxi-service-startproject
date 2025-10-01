from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car

from django.utils.translation import gettext_lazy as _


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
    search_fields = ["name", "country", ]


@admin.register(Driver)
class DriversAdmin(UserAdmin):
    list_display = [
        "license_number",
        "username",
        "email",
        "password",
        "first_name",
        "last_name", ]
    search_fields = [
        "license_number",
        "username",
        "email",
        "first_name",
        "last_name", ]
    fieldsets = UserAdmin.fieldsets + (
        (_("Additional info"), {"fields": ("license_number", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (_("Additional info"), {"fields": (
            "first_name",
            "last_name",
            "license_number", )}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        "model",
        "manufacturer", ]
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]
# Register your models here.
