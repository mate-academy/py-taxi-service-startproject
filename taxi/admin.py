from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver
    list_display = ('username', 'email', 'first_name', 'last_name', "license_number", "is_staff")
    search_fields = ('username', 'email', "license_number")
    ordering = ('username',)

    fieldsets = UserAdmin.fieldsets + (
    ('Additional Information', {'fields': ('license_number',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')
    ordering = ('name',)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)
    list_filter = ('manufacturer',)
    filter_horizontal = ('drivers',)
