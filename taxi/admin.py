from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from  taxi.models import Car, Driver, Manufacturer


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("licence_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {
            "fields": ("first_name", "last_name", "licence_number")
        }),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
