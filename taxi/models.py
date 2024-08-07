from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    country: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model: str = models.CharField(max_length=255)
    manufacturer: Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers: models.ManyToManyField = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number: str = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return f"{self.username}: ({self.first_name}, {self.last_name})"
