from django.contrib import admin
from .models import Manufacturer, Car, Driver

admin.site.site_header = 'Taxi Services'


class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'display_manufacturer', 'display_drivers')
    search_fields = ('model',)
    list_filter = ('manufacturer__name',)

    def display_manufacturer(self, obj):
        return obj.manufacturer.name

    display_manufacturer.short_description = 'Manufacturer'

    def display_drivers(self, obj):
        return ', '.join(driver.username for driver in obj.drivers.all())

    display_drivers.short_description = 'Drivers'


class DriverAdmin(admin.ModelAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'license_number',
    )
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Additional info', {'fields': ('license_number',)}),
        ('Permissions', {'fields': (
            'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'
        )}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'license_number')}
         ),
    )


admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
