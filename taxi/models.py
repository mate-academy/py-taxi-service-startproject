from pyexpat import model

from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        unique=True,
        on_delete=models.CASCADE,
        related_name="manufacturer_cars",
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="driver_cars"
    )

    def __str__(self):
        return f"{self.model} - {self.manufacturer}"
