from django.contrib import admin
from .models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin


class CarAdmin(admin.ModelAdmin):
    list_filter = ("model", "manufacturer")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "license_number")
    list_filter = ("username", "first_name", "last_name", "license_number")

    fieldsets = UserAdmin.fieldsets + (
        ("Additional Info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional Info", {"fields": ("license_number",)}),
    )


# Register your models here.
admin.site.site_header = "Taxi Service 'SafeMoon' Admin"
admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
