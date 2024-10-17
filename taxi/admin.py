from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Driver, Manufacturer, Car

# Register your models here.


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_filter = [
        "manufacturer",
    ]
    search_fields = [
        "model",
    ]


@admin.register(Driver)
class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = (UserAdmin.fieldsets +
                 (("Additional info", {"fields": ("license_number",)}),))
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Additional info", {"fields": ("license_number",
                                                      "first_name",
                                                      "last_name",)}),))


admin.site.register(Manufacturer)
