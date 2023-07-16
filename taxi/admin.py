from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer"]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
