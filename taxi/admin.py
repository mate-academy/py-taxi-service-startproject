from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


admin.site.register(Manufacturer)
@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    list_display = ("username", "email", "first_name", "last_name", "license_number")

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model", "manufacturer__name")
    list_filter = ("manufacturer",)
