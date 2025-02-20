from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Manufacturer)
class AdminManufacturer(admin.ModelAdmin):
    pass


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


@admin.register(Driver)
class AdminDriver(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)
