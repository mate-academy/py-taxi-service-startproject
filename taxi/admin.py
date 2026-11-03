from django.contrib import admin

from taxi.models import Car, Manufacturer, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name", "country",)


@admin.register(Driver)
class UserAdmin(admin.ModelAdmin):
    search_fields = ("license_number", "username", "email", "password", "first_name", "last_name")