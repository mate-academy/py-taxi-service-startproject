from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer",)
    search_fields = ("model",)


class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number", "first_name", "last_name", )}),)

# Register your models here.7
admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
