from django.contrib import admin
from .models import Driver, Car

class DriverAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'driver_license_number')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional info', {'fields': ('driver_license_number',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Additional info', {'fields': ('driver_license_number',)}),
    )

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'manufacturer')
    search_fields = ('model',)
    list_filter = ('manufacturer',)

admin.site.register(Driver, DriverAdmin)
admin.site.register(Car, CarAdmin)
