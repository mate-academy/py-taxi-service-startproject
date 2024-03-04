from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}: ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="mark"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"Model: {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return (
            f"{self.username}: ({self.first_name}, "
            f"{self.last_name}, "
            f"{self.email}, "
            f"{self.license_number})"
        )
