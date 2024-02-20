from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from taxi.models import Car, Manufacturer, Driver


admin.site.register(Manufacturer)
admin.site.register(Car)
admin.site.register(Driver, UserAdmin)
