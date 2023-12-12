from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

    def __str__(self) -> str:
        return self.username


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self) -> str:
        return self.model
