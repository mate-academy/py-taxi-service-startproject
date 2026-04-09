from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Car, Manufacturer, Driver


class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
