from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car

# Register your models here.


class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    list_display_links = ("username",)
    list_editable = ("license_number",)
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number",)}),)


class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacture",)


admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
