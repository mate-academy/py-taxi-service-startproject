from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer",]
    list_filter = ["manufacturer",]
    search_fields = ["model",]


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country",]


class DriverAdmin(admin.ModelAdmin):
    list_display = ["license_number", "username",]
    fieldsets = UserAdmin.fieldsets + (("Additional info", {
        "fields": ("license_number",)
    }),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {
        "fields": ("license_number",)
    }),)



admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Driver , DriverAdmin)




