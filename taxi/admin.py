from django.contrib import admin

from .models import Manufacturer, Driver, Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ["license_number", ]
    fieldsets = (("Additional info", {'fields': ('license_number',)}), )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


admin.site.register(Manufacturer)
