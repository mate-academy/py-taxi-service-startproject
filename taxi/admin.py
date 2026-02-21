# taxi/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Додаємо license_number у список водіїв
    list_display = UserAdmin.list_display + ("license_number",)

    # Додаємо секцію "Additional info" для редагування
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    # Додаємо секцію "Additional info" для створення нового водія
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)  # Обов'язково за ТЗ
    list_filter = ("manufacturer",)  # Обов'язково за ТЗ


admin.site.register(Manufacturer)  # Реєстрація для тесту AdminSiteManufacturerTests