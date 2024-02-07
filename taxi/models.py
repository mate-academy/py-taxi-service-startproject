from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
    )


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255, unique=True, null=True, blank=True
    )
