from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name + " placed in " + self.country


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.username + " with ID" + self.license_number


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        related_name="cars",
        null=True
    )
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return self.model
