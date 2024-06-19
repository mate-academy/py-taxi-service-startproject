from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {
        "fields":
        (
            "license_number",
        )
    }
                                                ),)


@admin.register(Car)
class CarAdmin(UserAdmin):
    search_fields = ("model",)
    list_filter = ["manufacturer", ]
    list_display = ('model', 'manufacturer',)
    filter_horizontal = ('drivers',)
    ordering = ("model",)


admin.site.register(Manufacturer)
