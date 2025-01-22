from django.contrib import admin
from .models import Manufacturer, Driver, Car
from django.contrib.auth.admin import UserAdmin


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "license_number",
        "first_name",
        "last_name"
    )

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {"fields": (
                "is_active", "is_superuser", "groups", "user_permissions"
            )},
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = (
        (
            "Additional info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password",
                    "license_number",
                    "email",
                    "first_name",
                    "last_name",
                ),
            },
        ),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)
