from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)  # пошук за моделлю
    list_filter = ('manufacturer',)  # фільтр за виробником
    autocomplete_fields = ('manufacturer',)
    filter_horizontal = ('drivers',)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'license_number',
        'is_staff',
    )
    search_fields = ('username', 'email', 'first_name', 'last_name', 'license_number')

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )
