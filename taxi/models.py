from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='cars')

    def __str__(self):
        return f"{self.model} - {self.manufacturer.name}"
