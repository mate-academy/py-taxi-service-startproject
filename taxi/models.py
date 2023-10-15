from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["first_name", "last_name", "username"]


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, default=1)
    drivers = models.ManyToManyField(AUTH_USER_MODEL)

    class Meta:
        ordering = ["model", "manufacturer"]
