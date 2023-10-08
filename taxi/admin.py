from django.contrib import admin

from taxi.models import Car, Manufacturer, Driver

admin.site.register(Car)
admin.site.register(Manufacturer)
admin.site.register(Driver)
