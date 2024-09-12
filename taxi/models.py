from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, blank=True, unique=True)
    username = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ["license_number"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}{self.username} {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["manufacturer"]

    def __str__(self):
        return f"{self.model} {self.manufacturer} {self.drivers}"
