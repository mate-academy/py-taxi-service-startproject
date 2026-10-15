from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Car, Driver, Manufacturer


class DriverAdmin(UserAdmin):
    list_display = ("username", "email", "license_number")
    fieldsets = (
        *UserAdmin.fieldsets,
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = (
        *UserAdmin.add_fieldsets,
        ("Additional info", {"fields": ("license_number",)}),
    )


class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer",)
    search_fields = ("model",)


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
