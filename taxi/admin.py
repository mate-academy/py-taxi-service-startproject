from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "driver")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver
    list_display = UserAdmin.list_display + ('license_number',)
    fieldsets = (UserAdmin.fieldsets +
                 (
                     ("Additional info", {"fields": ("license_number",)}),
                 ))
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (
                         ("Additional info", {"fields": (
                             "first_name",
                             "last_name",
                             "email",
                             "license_number",)}),
                     ))


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
