from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cars')

    class Meta:
        ordering = ("manufacturer", )

    def __str__(self) -> str:
        return f"{self.manufacturer} - {self.model}"
