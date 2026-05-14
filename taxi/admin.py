from django.contrib import admin

from taxi.models import Car, Driver, Manufacturer

admin.site.register(Car)
admin.site.register(Driver)
admin.site.register(Manufacturer)
