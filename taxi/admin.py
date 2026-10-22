from django.contrib import admin

from.models import Car, Driver, Manufacturer

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "license_number")
    
    fieldsets = (
        (None, {"fields": ("username",)}),
        ("Additional info", {"fields": ("license_number",)}),
    )
    
    add_fieldsets = (
        (None, {"fields": ("username", "password1", "password2")}),
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
