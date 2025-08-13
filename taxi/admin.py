from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name", "license_number",)
        }),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", "driver_count"]
    search_fields = ["model"]
    list_filter = ["manufacturer"]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related("manufacturer").prefetch_related("drivers")

    @admin.display(description="Drivers")
    def driver_count(self, obj):
        return obj.drivers.count()


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]
    search_fields = ["name"]
