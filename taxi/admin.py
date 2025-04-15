from django.contrib import admin
from taxi.models import Manufacturer, Driver, Car
from django.contrib.auth.admin import UserAdmin


class CarAdmin(admin.ModelAdmin):
    search_fields = ["model",]
    list_filter = ["manufacturer"]


admin.site.register(Manufacturer)
admin.site.register(Car)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = UserAdmin.list_display + ('license_number',)
