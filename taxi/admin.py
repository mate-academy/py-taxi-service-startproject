from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Car, Driver


class DriverAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "license_number",)
    search_fields = ("username", "first_name", "last_name", "email", "license_number",)
    fieldsets = (
        (str, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "license_number")}),
        ("Cars", {"fields": ("cars",)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "first_name", "last_name", "email", "license_number"),
        }),
    )


class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer",)
    list_filter = ("manufacturer",)
    search_fields = ("model",)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
