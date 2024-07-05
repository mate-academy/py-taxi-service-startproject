from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.DO_NOTHING,
                                        related_name="manufacturer")
    drivers = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                related_name="cars")
