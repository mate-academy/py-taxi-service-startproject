from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(to=Driver, related_name="cars")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
