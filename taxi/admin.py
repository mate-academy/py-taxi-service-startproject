from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Dodanie license_number do listy wyświetlanej w adminie
    list_display = UserAdmin.list_display + ("license_number",)
    
    # Dodanie license_number do formularza edycji (Punkt 6.3)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    
    # Dodanie license_number do formularza tworzenia (Punkt 6.4)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number", "first_name", "last_name")}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # Możliwość wyszukiwania po modelu (Punkt 6.5)
    search_fields = ["model"]
    # Możliwość filtrowania po producencie (Punkt 6.6)
    list_filter = ["manufacturer"]
    