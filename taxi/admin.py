from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Car, Driver, Manufacturer


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    list_display = UserAdmin.list_display + ("license_number",)
    search_fields = ("username", "email", "license_number")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)
    list_filter = ('manufacturer',)
