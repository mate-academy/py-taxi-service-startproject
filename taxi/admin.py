from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Manufacturer, Driver, Car

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ('username', 'email', 'license_number', 'is_staff')
    search_fields = ('username', 'email', 'license_number')
    list_filter = ('is_staff', 'is_superuser', 'groups')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('license_number',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Additional info', {'fields': ('license_number',)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)
    list_filter = ('manufacturer',)


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    pass
