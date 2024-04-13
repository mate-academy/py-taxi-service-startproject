from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


class DriverAdmin(UserAdmin):
    model = Driver
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )
    list_display = list(UserAdmin.list_display) + ['license_number']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer']
    search_fields = ['model']
    list_filter = ['manufacturer']


admin.site.register(Driver, DriverAdmin)
