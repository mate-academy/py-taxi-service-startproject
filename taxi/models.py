from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=128)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return f"{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
