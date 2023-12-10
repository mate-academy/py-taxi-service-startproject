from django.contrib import admin
from taxi.models import Manufacturer, Driver, Car

admin.site.register(Manufacturer)


class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "license_number",
        "password",
        "additional_info",
    )
    search_fields = ("username", "email", "first_name", "last_name", "license_number")
    fieldsets = (
        (
            "Personal Information",
            {"fields": ("username", "email", "first_name", "last_name", "password")},
        ),
        (
            "Additional Info",
            {
                "classes": ("wide",),
                "fields": (
                    "license_number",
                    "additional_info",
                ),
            },
        ),
    )


admin.site.register(Driver, DriverAdmin)


class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


admin.site.register(Car, CarAdmin)
