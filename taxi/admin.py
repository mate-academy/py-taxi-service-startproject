from django.contrib import admin
from .models import Driver, Car, Manufacturer

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'license_number', 'email', 'first_name', 'last_name')

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    filter_horizontal = ('drivers',)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
