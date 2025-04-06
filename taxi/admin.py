from django.contrib import admin
from .models import Driver, Manufacturer, Car

class DriverAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'password')
        }),
        ('Additional info', {
            'fields': ('license_number',)
        }),
    )
    add_fieldsets = (
        (None, {
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        }),
        ('Additional info', {
            'fields': ('license_number',)
        }),
    )
    list_display = ('username', 'first_name', 'last_name', 'license_number', 'is_staff', 'is_active')
    search_fields = ('username', 'first_name', 'last_name', 'license_number')
    list_filter = ('is_staff', 'is_active')

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer', 'display_drivers')
    search_fields = ('model',)
    list_filter = ('manufacturer',)

    def display_drivers(self, obj):
        return ", ".join([driver.username for driver in obj.drivers.all()])
    display_drivers.short_description = 'Drivers'

admin.site.register(Driver, DriverAdmin)
admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
