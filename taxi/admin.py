from django.contrib import admin
from taxi.models import Driver, Car, Manufacturer
from django.contrib.auth.admin import UserAdmin


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (*UserAdmin.list_display, "license_number")
    add_fieldset = (*UserAdmin.add_fieldsets, ("Additional info", {"fields": ("license_number",)}))

    fieldsets = (*UserAdmin.fieldsets, ("Additional info", {"fields": ("license_number",)}))


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "manufacturer", "model")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass