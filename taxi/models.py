from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=55, unique=True)
    country = models.CharField(max_length=55)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=55, unique=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.username}"


class Car(models.Model):
    model = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(to=Manufacturer,
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.manufacturer.name}, {self.model}"
