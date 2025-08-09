from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} country: {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=100,
        unique=True,
        null=True,
        blank=True
    )
    class Meta:
        verbose_name_plural = "Drivers"

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
