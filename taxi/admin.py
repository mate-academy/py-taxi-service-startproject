from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", ]
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


@admin.register(Driver)
class AuthorAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {
        "fields": ("license_number",)
    }), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": (
        "first_name",
        "last_name",
        "email",
        "license_number",
    )}), )


admin.site.register(Manufacturer)
