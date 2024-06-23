from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    extra_fieldsets = (("Additional info", {"fields": ("license_number",)}),)
    fieldsets = UserAdmin.fieldsets + extra_fieldsets
    add_fieldsets = UserAdmin.add_fieldsets + extra_fieldsets


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
    list_filter = ("country",)
