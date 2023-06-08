from django.contrib import admin
from .models import Driver, Car, Manufacturer


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ("license_number", "username", "email", "password", "first_name", "last_name")
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "first_name", "last_name")}),
        ('Additional info', {'fields': ('license_number',)}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "password1", "password2", "email", "license_number"),
        }),
    )


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_field = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Manufacturer)
