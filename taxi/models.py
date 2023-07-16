from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.last_name} {self.first_name})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        null=True,
        on_delete=models.SET_NULL,
        related_name="cars",
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
