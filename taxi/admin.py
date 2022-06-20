from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("License info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("License info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class Car(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = filter = ["manufacturer"]


admin.site.register(Manufacturer)
