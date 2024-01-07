from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import  Car, Manufacturer, Driver

class DriverAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number",)
    fieldsets = UserAdmin.fieldsets + (
        ("Additional info",
         {
             "classes" : ("collapse",),
             "fields" : (("license_number",),)
         }
         ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Additional info",
         {
             "fields" : (("license_number",),)
         }
         ),
    )

class CarAdmin(admin.ModelAdmin):
    search_fields = ("model",)
    list_filter = ("manufacturer",)


admin.site.register(Car, CarAdmin)
admin.site.register(Manufacturer)
admin.site.register(Driver, DriverAdmin)
