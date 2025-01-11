from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


# Create your models here.


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class Car(models.Model):
    model_name = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="car",
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="car")

    def __str__(self) -> str:
        return self.model_name
