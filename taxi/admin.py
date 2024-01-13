from django.contrib import admin

from taxi.models import Driver, Manufacturer, Car

from django.contrib.auth.admin import UserAdmin


class DriverAdmin(UserAdmin):
    model = Driver
    list_display = UserAdmin.list_display + (
        "license_number",
    )

    fieldsets = UserAdmin.fieldsets + (
        ("Additional info", {"fields":("license_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info", {"fields":("license_number",)}),
    )


class CarAdmin(admin.ModelAdmin):
    search_fields = ['model']
    list_filter = ['manufacturer']


admin.site.register(Driver, DriverAdmin)
admin.site.register(Manufacturer)
admin.site.register(Car, CarAdmin)
