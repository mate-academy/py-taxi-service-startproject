from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return (
            f"name: {self.first_name}, "
            f"surname: {self.last_name}, "
            f"license number: {self.license_number}"
        )


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="Cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="Cars"
    )

    def __str__(self) -> str:
        return (
            f"Model: {self.model}, "
            f"Manufacturer: {self.manufacturer}"
        )
