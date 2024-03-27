from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=67, unique=True)
    country = models.CharField(max_length=67)

    def __str__(self) -> str:
        return f"{self.country} - {self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=37, unique=True, null=True, blank=True)


class Car(models.Model):
    model = models.CharField(max_length=67)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.model}, {self.manufacturer}, {self.drivers}"
