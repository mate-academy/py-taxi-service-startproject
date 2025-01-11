from django.contrib import admin

from taxi.models import Driver, Manufacturer, Car

from django.contrib.auth.admin import UserAdmin

# Register your models here.


admin.site.register(Manufacturer)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model_name", "manufacturer", ]
    list_filter = ["manufacturer", ]
    search_fields = ["model_name", ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number", )}), )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {
        "fields": (
            "first_name", "last_name", "license_number",)}),)
