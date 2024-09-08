from django.contrib import admin
from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)
    ordering = ("model",)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "license_number")
    search_fields = ("username", "email", "license_number")
    ordering = ("license_number",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("license_number",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("license_number",)}),
    )
