from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


from taxi.models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('license_number',)
    fieldsets = UserAdmin.fieldsets + (("Additional", {"fields": ("license_number", )}),)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = [
        'model'
    ]
    search_fields = ['model']
    list_filter = ['manufacturer']


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'country',
    ]
