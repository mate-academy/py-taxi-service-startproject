from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver
    list_display = (UserAdmin.list_display +
                    ("license_number", ))
    fieldsets = (UserAdmin.fieldsets +
                 (("Additional info", {"fields": ("license_number", )}),))
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Additional info", {"fields": ("license_number",)}),))


admin.site.register(Manufacturer)
