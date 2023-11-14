from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name_plural = "Drivers"

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.model}"
