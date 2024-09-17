from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
    )

    class Meta:
        ordering = ["license_number"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="cars",
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model
