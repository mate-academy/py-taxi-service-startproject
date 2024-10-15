from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm, PasswordInput
from taxi.models import Car, Manufacturer, Driver


class UserForm(ModelForm):
    class Meta:
        widgets = {'password': PasswordInput, }


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info", {"fields": ("license_number",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("license_number", )}), )
    form = UserForm


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = ("manufacturer", )
    search_fields = ("model", )


admin.site.register(Manufacturer)
