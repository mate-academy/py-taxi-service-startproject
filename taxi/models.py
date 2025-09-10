from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    class Meta:
        ordering = ('name',)

class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        "Driver", related_name="cars", blank=True

    )
    class Meta:
        unique_together = ("model", "manufacturer")
        ordering = ("manufacturer__name", "model")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
