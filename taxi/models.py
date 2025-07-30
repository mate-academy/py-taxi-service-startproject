from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number: str = models.CharField(max_length=20, unique=True)


class Manufacturer(models.Model):
    name: str = models.CharField(max_length=63, unique=True)
    country: str = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f'{self.name} ({self.country})'


class Car(models.Model):
    model: str = models.CharField(max_length=63)
    manufacturer: models.ForeignKey = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(Driver)

    def __str__(self) -> str:
        return self.model
