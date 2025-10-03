from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    my_field_set = (
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )
    add_fieldsets = fieldsets = UserAdmin.fieldsets + my_field_set
    # fieldsets = UserAdmin.fieldsets + my_field_set

    list_display = ["first_name", "last_name", "license_number"]


@admin.register(Car)
class UserCar(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class UserManufacturer(admin.ModelAdmin):
    list_display = (
        "name",
        "country",
    )
