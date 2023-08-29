from django.contrib import admin
from .models import Car, Driver, Manufacturer


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ["model"]
    list_filter = ["manufacturer"]


class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "license_number",
        "username",
        "email",
        "first_name",
        "last_name"
    )
    fieldsets = (
        (None, {
            'fields': ("username", "email", "first_name", "last_name")
        }),
        ("Additional info", {
            'classes': ("collapse",),
            'fields': ("license_number",),
        }),
    )


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
