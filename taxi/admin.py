from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("license_number",) + UserAdmin.list_display
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ((
        "Additional info",
        {
            "classes": ("wide",),
            "fields": ("license_number",)
        }
    ),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Manufacturer)
