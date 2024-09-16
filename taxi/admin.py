from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    search_fields = ["model"]
    list_filter = ["manufacturer__name"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)

    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("license_number", )}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("first_name", "last_name")}),
        ("Additional information", {"fields": ("license_number",)}),
    )


admin.site.register(Manufacturer)
