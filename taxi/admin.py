from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        "license_number",
        "username",
        "email",
        "first_name",
        "last_name",
        "password",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)
    list_display = ("model",)


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    fieldsets = (
        (
            "Manufacturer Information",
            {"fields": ("name", "country")},
        ),
    )
