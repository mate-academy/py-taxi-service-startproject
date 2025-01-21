from django.contrib import admin
from .models import Manufacturer, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']
    list_filter = ['manufacturer']

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'license_number')

    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password', 'first_name', 'last_name'),
        }),
        ('Additional info', {
            'fields': ('license_number',),
        }),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'password1', 'password2', 'first_name', 'last_name'),
        }),
        ('Additional info', {
            'fields': ('license_number',),
        }),
    )

    search_fields = ('license_number', 'username', 'email')

admin.site.register(Manufacturer)
