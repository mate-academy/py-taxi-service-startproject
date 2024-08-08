from django.contrib import admin

from taxi.models import Manufacturer, Driver, Car


class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "license_number")
    fieldsets = (
        ("Additional info", {
            "fields": ("license_number",)
        }),
    )
    add_fieldsets = (
        ("Additional info", {
            "fields": ("license_number",)
        }),
    )


class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer",)
    search_fields = ("model",)


admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
