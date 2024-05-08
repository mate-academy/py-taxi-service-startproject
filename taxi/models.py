from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=63, unique=True
    )
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=50, unique=True
    )

    class Meta:
        ordering = ("last_name",)
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(to=Driver)

    class Meta:
        ordering = ("manufacturer",)
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
