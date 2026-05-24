from django.contrib import admin

from .models import Manufacturer, Driver, Car

admin.site.register(Manufacturer)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["license_number"]

    fieldsets = (
        (None, {
            "fields": ("username", "password", "first_name", "last_name", "email")
        }),
        ("Additional info", {
            "fields": ("license_number",)
        }),
    )

    add_fieldsets = (
        (None, {
            "fields": ("username", "password", "first_name", "last_name", "email")
        }),
        ("Additional info", {
            "fields": ("license_number",)
        }),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]

    search_fields = ["model"]
    list_filter = ["manufacturer"]
