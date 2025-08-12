from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from taxi.models import Driver, Manufacturer, Car

# admin.site.register(Manufacture)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('name',)}),
    )
    list_display = ("name", "country")


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    model = Driver

    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    list_display = UserAdmin.list_display + ('license_number',)


@admin.register(Car)
class AdminCar(admin.ModelAdmin):
    search_fields = ("model", )
    list_filter = ('manufacturer',)
    list_display = ("model", "manufacturer")
