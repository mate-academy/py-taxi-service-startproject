from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    add_fieldsets = UserAdmin.add_fieldsets + ( ( "Additional info", { "fields": ("license_number",) } ), )
    fieldsets = UserAdmin.fieldsets + ( ( "Additional info", { "fields": ("license_number",) } ), )
    list_display = UserAdmin.list_display + ("license_number",)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model",]
    list_filter = ["manufacturer",]
