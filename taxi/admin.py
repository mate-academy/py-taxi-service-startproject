from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Manufacturer, Driver, Car


class DriverAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("license_number",)

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Additional info", {"fields": ("license_number",)}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "license_number"),
        }),
    )


class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ["name"]


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
