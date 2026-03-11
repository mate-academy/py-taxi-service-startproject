from django.contrib import admin
from taxi.models import Driver,Manufacturer, Car
from django.contrib.auth.admin import UserAdmin

class DriverAdmin(UserAdmin):
    list_display = ("username", "first_name", "last_name", "email", "license_number", "is_staff",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields": ("license_number",)}),
    )

class CarAdmin(admin.ModelAdmin):
    list_display = ("manufacturer", "model", "get_drivers",)
    search_fields = ("model",)
    list_filter = ("manufacturer",)

    def get_drivers(self, obj):
        return ",".join(str(d) for d in obj.drivers.all())
    get_drivers.short_description = "Drivers"

admin.site.register(Driver,DriverAdmin)
admin.site.register(Manufacturer)
admin.site.register(Car,CarAdmin)
