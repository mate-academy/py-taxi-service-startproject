from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self):
        return f"{self.model} by {self.manufacturer.name}"
