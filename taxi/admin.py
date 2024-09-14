from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Driver, Car


class DriverAdmin(UserAdmin):
    list_display = ("first_name", "last_name", "email", "license_number")
    search_fields = ("first_name", "last_name", "email", "license_number")
    list_filter = ("first_name", "last_name", "email", "license_number")
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model")
    search_fields = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
