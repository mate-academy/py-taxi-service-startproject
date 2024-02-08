from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=20,
        unique=True
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=250)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return (
            f"Model: {self.model} "
            f"Manufacturer: {self.manufacturer}"
        )
