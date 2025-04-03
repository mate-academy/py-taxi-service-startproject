from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=82)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        model = self.model or "<MODEL>"
        manufacturer = self.manufacturer or "<MANUFACTURER>"
        return f"{manufacturer} {model}"
