from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Manufacturer, Car, Driver

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'license_number')
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
            ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    list_filter = ("manufacturer",)
    search_fields = ("model",)

admin.site.register(Manufacturer)
