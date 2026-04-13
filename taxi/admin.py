from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class AdminDriver(admin.ModelAdmin):
    list_display = ["license_number",
                    "username",
                    "email",
                    "password",
                    "first_name",
                    "last_name",
                    ]
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    list_display = ("name", "country")
    list_filter = ("name",)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model", "manufacturer__name")
