from django.contrib import admin
from .models import Driver, Car, Manufacturer
from django.contrib.auth.admin import UserAdmin
from django.conf import settings

admin.site.register(Manufacturer)

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (('Additional info', {'fields': ('license_number',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ["model"]
    list_filter = ["manufacturer"]
