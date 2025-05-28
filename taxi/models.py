from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()


class Driver(AbstractUser):
    license_number = models.CharField(unique=True)


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
