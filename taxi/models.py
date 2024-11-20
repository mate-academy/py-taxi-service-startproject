from django.contrib.auth.models import AbstractUser

from django.db import models
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return f"{self.model} {self.manufacturer}, drivers: ({self.drivers})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name_plural = "drivers"
        verbose_name = "driver"

    def __str__(self) -> str:
        return (f"({self.first_name}, {self.last_name}),"
                f" license_number: {self.license_number}")
