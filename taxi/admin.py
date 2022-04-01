from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacture, Car


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Add license number", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Add additional info and license number",
            {"fields": ("first_name", "last_name", "license_number")}
        ),
    )
