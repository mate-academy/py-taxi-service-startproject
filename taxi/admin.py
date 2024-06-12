from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = UserAdmin.list_display + ("license_number",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["manufacturer", "model"]
    search_fields = ["model",]
    list_filter = ["manufacturer",]


admin.site.register(Manufacturer)


