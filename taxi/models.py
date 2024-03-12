from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}. (Country: {self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
