from django.contrib import admin
from .models import Manufacturer, Car, Driver

# Register your models here.
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model", )
    list_filter = ("manufacturer", )



@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("license_number", "username", "email", "first_name", "last_name", "password")
    fieldsets = [
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password')
        }),
        ("Additional info", {
            'fields': ('license_number',)
        }),
    ]
    add_fieldsets = [
        (None, {
            'fields': ('username', 'email', 'password')
        }),
        ("Additional info", {
            'fields': ('license_number',)
        }),
    ]
