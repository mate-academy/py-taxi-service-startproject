from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


admin.site.register(Manufacturer)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = (
        "username",
        "license_number",
        "first_name",
        "last_name",
        "is_staff",
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)
