import django

from django.contrib import admin

class Manufacturer(django.db.models.Model):
    name = django.db.models.CharField()
    country = django.db.models.CharField()
