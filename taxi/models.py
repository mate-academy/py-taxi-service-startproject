from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    # se quiser exigir na CLI do createsuperuser:
    REQUIRED_FIELDS = ["email", "license_number"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.username} ({self.license_number})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField("Driver", related_name="cars", blank=True)

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:  # pragma: no cover
        return f"{self.model} — {self.manufacturer.name}"
