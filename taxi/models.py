from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.license_number})"
