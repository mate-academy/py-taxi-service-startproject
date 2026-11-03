from django.contrib import admin

from taxi.models import Car


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    search_fields = ('model',)
    list_filter = ('manufacturer',)