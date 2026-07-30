from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Manufacturer, Car

class DriverAdmin(UserAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "license_number",
    )
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
admin.site.register(Driver, DriverAdmin)
admin.site.register(Manufacturer)


class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)
admin.site.register(Car, CarAdmin)
