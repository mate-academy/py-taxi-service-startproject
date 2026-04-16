from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Driver, Car, Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "country")
    search_fields = ("name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver

    list_display = (
        "id",
        "username",
        "license_number",
        "is_staff",
    )

    search_fields = (
        "username",
        "license_number",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "model", "manufacturer")
    search_fields = ("model", "manufacturer")
    list_filter = ("manufacturer",)
