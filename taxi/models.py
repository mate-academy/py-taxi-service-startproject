from django.db import models

from taxi_service.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name",)
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="car"
    )

    def __str__(self) -> str:
        return f"{self.manufacturer} - {self.model}"

    class Meta:
        ordering = ("model",)
        verbose_name = "car"
        verbose_name_plural = "cars"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True, null=True, blank=True)

    class Meta:
        ordering = (
            "first_name",
            "last_name",
        )
        verbose_name = "driver"
        verbose_name_plural = "drivers"
