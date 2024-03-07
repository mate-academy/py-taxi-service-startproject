from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}. (Country: {self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}. (License: {self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(to=AUTH_USER_MODEL, related_name="drivers")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
