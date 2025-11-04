from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    """
    Налаштування для моделі Driver в адмін-панелі.
    Додає license_number до list_display, fieldsets та add_fieldsets.
    """
    list_display = UserAdmin.list_display + ("license_number",)
    
    # Додаємо 'Additional info' до fieldsets (для сторінки редагування)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    
    # Додаємо 'Additional info' до add_fieldsets (для сторінки створення)
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    """
    Налаштування для моделі Car в адмін-панелі.
    Додає пошук за моделлю та фільтр за виробником.
    """
    search_fields = ("model",)
    list_filter = ("manufacturer",)


# Реєструємо Manufacturer з базовими налаштуваннями
admin.site.register(Manufacturer)
