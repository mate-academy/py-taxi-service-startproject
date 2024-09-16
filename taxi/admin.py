from django.contrib import admin

from taxi.models import Car, Driver, Manufacturer


# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer",)
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = (
        "license_number",
        "username",
        "first_name",
        "last_name",
        "email",
    )

    fieldsets = [
        (
            "Add Driver",
            {
                "fields": [
                    "username",
                    "email",
                    "first_name",
                    "last_name",
                    "password",
                ]
            }
        ),
        (
            "Additional info",
            {
                "fields": [
                    "license_number",
                ]
            }
        )

    ]

    add_fieldsets = (
        "Additional info", {
            "fields": [
                "license_number",
            ]
        }
    )
    
    


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
