from django.contrib import admin

from taxi.models import Car, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name", "country",)