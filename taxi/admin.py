from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
from taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ('manufacturer',)
    search_fields = ('model',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info",
        {
            "fields": (
                "license_number",
            ),
        }
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info",
        {
            "fields": (
                "first_name",
                "last_name",
                "license_number",
            )
        }
        ),
    )
