from django.contrib import admin
from .models import Manufacturer, Car, Driver

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'license_number')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'first_name', 'last_name', 'email')}),
        ('Additional info', {'fields': ('license_number',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'license_number'),
        }),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    list_filter = ('manufacturer',)
    search_fields = ('model',)

admin.site.register(Manufacturer)
