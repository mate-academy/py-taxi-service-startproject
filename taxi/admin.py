from django.contrib import admin
from taxi.models import Car, Manufacturer, Driver
from django.contrib.auth.admin import UserAdmin


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = (
        (
            "Additional info",
            {
                "fields": ("username", "password")
            }
        ),
        (
            "Personal Info",
            {
                "fields": (
                    "license_number",
                    "first_name",
                    "last_name",
                    "email"
                )
            }
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions"
                )
            }
        ),
        (
            "Important dates",
            {
                "fields": (
                    "last_login",
                    "date_joined"
                )
            }
        ),
    )
    add_fieldsets = (
        (
            "Additional info",
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "license_number"
                ),
            }
        ),

    )
    list_display = (
        "username",
        "first_name",
        "last_name",
        "license_number",
        "email",
        "is_staff"
    )
    search_fields = (
        "username",
        "first_name",
        "last_name",
        "license_number"
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country",)
