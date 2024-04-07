from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
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


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer", "driver")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


# Register your models here.
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
