from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


class DriverAdmin(UserAdmin):
    list_display = ("username", "email", "license_number")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("email",)}),
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
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
                "fields": ("username", "email", "password1", "password2"),
            },
        ),
        (
            "Additional info",
            {"fields": ("license_number",)},
        ),
    )


class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
