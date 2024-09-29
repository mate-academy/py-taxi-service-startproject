from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Car, Driver


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        "license_number",
        "username",
        "username",
        "email",
        "first_name",
        "last_name"
    )
    fieldsets = (UserAdmin.fieldsets +
                 (("Additional info", {"fields": ("license_number",)}),))
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Additional info", {"fields": ("license_number",)}),))


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model", )
    list_filter = ("manufacturer", )


admin.site.register(Manufacturer)
