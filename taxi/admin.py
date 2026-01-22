from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Manufacturer, Car, Driver


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Display license_number in the general list of drivers
    list_display = UserAdmin.list_display + ('license_number',)

    # Additional info category when updating (editing) Driver
    fieldsets = UserAdmin.fieldsets + (
    ('Additional info', {'fields': ('license_number',)}),
    )

    # "Additional info" category when adding (creating) a Driver
    add_fieldsets = UserAdmin.add_fieldsets + (
    ('Additional info', {'fields': ('license_number',)}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ('model',)

    list_filter = ('manufacturer',)

admin.site.register(Manufacturer)
