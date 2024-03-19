from django.contrib import admin
from taxi.models import Manufacturer, Car, Driver
from django.contrib.auth.admin import UserAdmin
# Register your models here.


@admin.register(Driver)
class Driver(UserAdmin):
    list_display = UserAdmin.list_display + ("license_number", )
    fieldsets = UserAdmin.fieldsets + (("Additional info",
                                        {"fields": ("license_number", )}), )
    add_fieldsets = (UserAdmin.add_fieldsets +
                     (("Additional info", {"fields": ("license_number", )}), ))


@admin.register(Car)
class Car(admin.ModelAdmin):
    list_filter = ["manufacturer", ]
    search_fields = ["model", ]


admin.site.register(Manufacturer)
