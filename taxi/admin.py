from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufactured


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufactured", "drivers_list", ]
    search_fields = ["model", ]
    list_filter = ["manufactured", ]

    def drivers_list(self, drive):
        return ", ".join([driver.username for driver in drive.drivers.all()])


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldset = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


@admin.register(Manufactured)
class ManufacturedAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]
