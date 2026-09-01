from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from taxi.models import Manufacturer, Driver, Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['model', 'manufacturer',"display_drivers"]
    list_filter = ["manufacturer",]
    search_fields = ['model', 'manufacturer__name',]

    @admin.display(description='Drivers')
    def display_drivers(self, obj):
        return ", ".join([driver.username for driver in obj.driver.all()])

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'country',]
    search_fields = ['name', 'country', ]
    list_filter = ['name', 'country', ]

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)

