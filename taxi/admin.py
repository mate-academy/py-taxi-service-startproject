from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name", "country")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    search_fields = ("license_number", "username", "email", "first_name", "last_name")
    list_display = ("username", "license_number", "is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2"),
        }),
        ("Additional info", {
            "fields": ("license_number",),
        }),
    )
