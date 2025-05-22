from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = [
            "name",
        ]
        verbose_name_plural = "Manufacturers"
        verbose_name = "Manufacturer"

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=60, unique=True, verbose_name="License Number"
    )

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return (
            f"{full_name if full_name else self.username}"
            f" (License: {self.license_number})"
        )


class Car(models.Model):
    model = models.CharField(max_length=255)
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars_assign",
        verbose_name="Driver",
    )

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        verbose_name="Manufacturer",
        related_name="cars",
    )

    class Meta:
        ordering = ["model", "manufacturer"]
        verbose_name_plural = "Cars"
        verbose_name = "Car"

    def __str__(self):
        return f"{self.manufacturer.name} ({self.model})"
