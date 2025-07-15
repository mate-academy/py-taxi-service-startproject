from django.contrib import admin
from .models import Driver, Car, Manufacturer

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name",
                    "last_name", "email", "license_number")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Permissions", {"fields": ("is_active",
                                    "is_staff", "is_superuser",
                                    "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
        ("Additional info", {"fields": ("license_number",)}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)

admin.site.register(Manufacturer)
