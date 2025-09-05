from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Manufacturer, Car


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Display license_number in the list view
    list_display = ('username',
                    'email',
                    'first_name',
                    'last_name',
                    'license_number',
                    'is_staff')

    # Add license_number under 'Additional info' in edit form
    fieldsets = UserAdmin.fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )

    # Add license_number under 'Additional info' in add form
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional info', {'fields': ('license_number',)}),
    )


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')
    search_fields = ('name', 'country')


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer',)
    search_fields = ('model',)
    list_filter = ('manufacturer',)
