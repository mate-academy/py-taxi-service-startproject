from django.contrib import admin
from taxi.models import Driver, Manufacturer, Car
from django.contrib.auth.admin import UserAdmin


# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("id", "first_name", "last_name", "license_number")
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )