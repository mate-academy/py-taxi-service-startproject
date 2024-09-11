from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (("Additional info", {
            "fields": ("license_number",)}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufactured"]
    search_fields = ["model"]


admin.site.register(Manufacturer)
