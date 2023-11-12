from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional information", {"fields": ("license_number", )}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional information", {"fields": ("license_number", )}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model", ]
    list_filter = ["manufacturer", ]


admin.site.register(Manufacturer)
