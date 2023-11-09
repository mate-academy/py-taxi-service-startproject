from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, null=True, blank=True, unique=True)
    username = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ["license_number"]

    def __str__(self):
        return f"{self.username} {self.license_number} {self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars",)

    class Meta:
        ordering = ["manufacturer"]

    def __str__(self):
        return f"{self.model} {self.manufacturer} {self.drivers}"
