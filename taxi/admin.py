from django.contrib import admin
from .models import Car, Manufacturer, Driver


class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']
    list_filter = ['manufacturer']


class DriverAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Additional info', {'fields': ('license_number', 'car')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'password1', 'password2')}),
        ('Additional info', {'fields': ('license_number', 'car')}),
    )
    list_display = ['username', 'license_number']
    search_fields = ['license_number']


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
