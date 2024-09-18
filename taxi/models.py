from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=300, unique=True)
    country = models.CharField(max_length=300)

    def __str__(self) -> str:
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=300)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=300, unique=True)

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name}, {self.last_name}"
