from django.contrib import admin
from taxi.models import Car, Manufacturer, Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'license_number']
    fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password')
        }),
        ('Additional info', {
            'classes': ('collapse',),  # Це дозволяє приховувати секцію за замовчуванням
            'fields': ('license_number',),  # Додаємо поле license_number до цієї секції
        }),)
    add_fieldsets = (
        (None, {
            'fields': ('username', 'email', 'first_name', 'last_name', 'password')
        }),
        ('Additional info', {
            'classes': ('collapse',),
            'fields': ('license_number',),  # Додаємо поле license_number до цієї секції для форми додавання
        }),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']
    list_filter = ['manufacturer']


admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
admin.site.register(Driver, DriverAdmin)
