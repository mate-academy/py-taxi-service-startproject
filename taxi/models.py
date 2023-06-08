from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=64)
    country = models.CharField(max_length=64)

    def __str__(self) -> str:
        return str(self.name)

    class Meta:
        constraints = [models.UniqueConstraint(fields=("name",), name="name_unique")]
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("license_number",), name="license_number_unique"
            )
        ]
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="manufacturer", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        AUTH_USER_MODEL,
        related_name="cars",
    )

    class Meta:
        ordering = ["manufacturer", "model"]
