# taxi/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Car, Manufacturer

# 1. Registrar Manufacturer
@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


# 2. Registrar Driver (Extende UserAdmin)
@admin.register(Driver)
class DriverAdmin(UserAdmin):
    # Para exibir license_number na lista de usuários
    list_display = ('username', 'email', 'first_name', 'last_name', 'license_number', 'is_staff')

    # Configurações para a página de ADICIONAR (add_fieldsets)
    add_fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Additional info', {'fields': ('license_number',)}), # <-- ADICIONAR AQUI
    )

    # Configurações para a página de EDITAR (fieldsets)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',
                                   'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Additional info', {'fields': ('license_number',)}), # <-- ADICIONAR AQUI
    )


# 3. Registrar Car
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'license_plate', 'manufacturer')
    search_fields = ('model',) # <-- Permitir busca por model
    list_filter = ('manufacturer',) # <-- Permitir filtro por manufacturer
