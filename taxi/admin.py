from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Manufacturer, Car, Driver


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Licence", {"fields": ("licence_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Licence", {"fields": ("licence_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


admin.site.register(Manufacturer)
