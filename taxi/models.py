from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey, ManyToManyField

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE
    )
    drivers = ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
