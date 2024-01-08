from django.contrib import admin
from taxi.models import Driver, Manufacturer, Car
from django.contrib.auth.admin import UserAdmin


class DriverAdmin(UserAdmin):
    model = Driver
    list_display = ['username', 'email', 'license_number']

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('email', 'first_name', 'last_name')}),
        ('Additional info', {'fields': ('license_number',)}),  # Include license_number in 'Additional info'
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'license_number')},
         ),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']
    list_filter = ['manufacturer']


admin.site.register(Driver, DriverAdmin)
admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
