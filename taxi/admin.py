from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import DriverCreationForm, DriverChangeForm
from .models import Manufacturer, Driver, Car

@admin.register(Driver)
class DriverAdmin(UserAdmin):
    add_form = DriverCreationForm
    form = DriverChangeForm
    model = Driver

    list_display = ("username", "first_name", "last_name", "email", "license_number", "is_staff")
    search_fields = ("username", "first_name", "last_name", "email", "license_number")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("license_number",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("username", "password1", "password2")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        ("Additional info", {"fields": ("license_number",)}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups")}),
    )

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("model", "manufacturer")
    search_fields = ("model",)
    list_filter = ("manufacturer",)

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    search_fields = ("name",)
