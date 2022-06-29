from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Car, Manufacturer


class DriversInline(admin.TabularInline):
    model = Car.drivers.through
    extra = 1


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ['country']
    search_fields = ['name']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer', 'all_drivers']
    list_filter = ['manufacturer']
    search_fields = ['model']
    inlines = (DriversInline,)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('license_number', 'password')
    fieldsets = UserAdmin.fieldsets + (("Extra info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + \
                    (("Extra info", {"fields": ("first_name", "last_name", "email", "license_number",)}),)
    inlines = (DriversInline,)
