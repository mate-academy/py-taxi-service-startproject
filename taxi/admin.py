from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Driver, Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer"]
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Licence data", {"fields": ("licence_number", )}, ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal info",
         {"fields": ("first_name", "last_name", "email", "licence_number",)},),
    )


admin.site.register(Manufacturer)


