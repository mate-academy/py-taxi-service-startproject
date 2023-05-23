from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                fields=["name", ],
                name="unique_constraint_name"
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["manufacturer"]

    def __str__(self) -> str:
        return f"{self.model} - {self.manufacturer.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        constraints = [
            UniqueConstraint(
                fields=["license_number", ],
                name="unique_constraint_license_number"
            )
        ]

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"
