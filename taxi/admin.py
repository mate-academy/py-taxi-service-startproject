from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Driver, Manufacturer, Car

# Register your models here.


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = list(UserAdmin.list_display) + ["license_number",]

    fieldsets = list(UserAdmin.fieldsets) + [
        ("Additional info", {"fields": ("license_number",)}),
    ]

    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ("Additional info", {"classes": ("wide",), "fields": ("license_number",)}),
    ]


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ["name", "country", ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ["model", "manufacturer", ]
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]

# admin.site.register(Manufacturer)
# admin.site.register(Car)
