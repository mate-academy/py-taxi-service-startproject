from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("licence_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("licence_number",)}),
    )


@admin.register(Car)
class CarAdmin(ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


admin.site.register(Manufacturer)
