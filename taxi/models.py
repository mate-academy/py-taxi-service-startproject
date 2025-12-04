from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ManyToManyField

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ("last_name", "first_name")

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    driver = ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
    )
