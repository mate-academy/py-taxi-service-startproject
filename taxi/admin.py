from django.contrib import admin
from .models import Manufacturer, Car, Driver
# Register your models here.

@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "license_number")  # Відображення `license_number`
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        ("Additional info", {"fields": ("license_number",)}),  # Додавання `license_number` до групи "Additional info"
    )
    add_fieldsets = (
        (None, {"fields": ("username", "email", "password1", "password2")}),
        ("Additional info", {"fields": ("license_number",)}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)  # Дозволяє пошук за `model`
    list_filter = ("manufacturer",)  # Дозволяє фільтрацію за `manufacturer`

admin.site.register(Manufacturer)
