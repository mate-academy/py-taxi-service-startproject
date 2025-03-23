from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self: "Manufacturer") -> str:
        return f"{self.name}, {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self: "Car") -> str:
        return f"{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
