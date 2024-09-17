from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    country: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number: str = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model: str = models.CharField(max_length=255)
    manufacturer: Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return self.model
