from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("licence_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Licence information", {"fields": ("licence_number", )}, ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal information",
         {"fields": ("first_name", "last_name", "email", "licence_number",)},),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]


@admin.register(Manufacturer)
class Manufacturer(admin.ModelAdmin):
    pass
