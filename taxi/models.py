from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.constraints import UniqueConstraint

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    county = models.CharField(max_length=255)


    class Meta:
        constraints = [
            UniqueConstraint(fields=("name",), name="unique_manufacturer_name"),
        ]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)
    class Meta:
        constraints = [
            UniqueConstraint(fields=("license_number",), name="unique_license_number"),
        ]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="manufacturer")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")
