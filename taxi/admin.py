from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from taxi.models import Manufacture, Car, Driver


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ["manufacturer"]
    search_fields = ["model"]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Licence", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Licence", {"fields": ("license_number",)}),
    ) + (("Additional info", {"fields": ("first_name", "last_name",)}),)


admin.site.register(Manufacture)
