from django.db import models

from django.contrib.auth.models import AbstractUser

import taxi_service.settings


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="manufacture"
    )
    drivers = models.ManyToManyField(taxi_service.settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)
