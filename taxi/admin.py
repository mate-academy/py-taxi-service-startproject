from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Driver, Manufacturer


@admin.register(Manufacturer)
class ManufactureAdmin(admin.ModelAdmin):
    list_display = ("name", "country")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "license_number",
        "is_staff",)

    fieldsets = UserAdmin.fieldsets + (
        (
        "Additional info",
        {
            "fields": ("license_number",)
        }
    ),
    )

    add_fieldsets = (
    (
        None,
        {
            "classes": ("wide",),
            "fields": (
                "username",
                "password1",
                "password2",
            ),
        },
    ),
    (
        "Additional info",
        {
            "classes": ("wide",),
            "fields": ("license_number",),
        },
    ),
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:
            from django.contrib.auth.forms import UserCreationForm
            kwargs["form"] = UserCreationForm
        return super().get_form(request, obj, **kwargs)

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    list_filter = ("manufacturer",)
    search_fields = ("model",)
# Register your models here.
