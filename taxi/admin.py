from django.contrib import admin
from .models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin


class DriversAdmin(UserAdmin):
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'license_number',
    )

    fieldsets = UserAdmin.fieldsets + (
        (
            'Additional info',
            {'fields': ('license_number',)}
        ),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            'Additional info',
            {'fields': ('license_number',)}
        ),
    )

class CarAdmin(admin.ModelAdmin):
    search_fields = ('model',)
    list_filter = ('manufacturer',)

admin.site.register(Manufacturer)
admin.site.register(Driver, DriversAdmin)
admin.site.register(Car, CarAdmin)
