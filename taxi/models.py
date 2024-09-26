from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name = "Drives"
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.model} {self.manufacturer}"
