from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self: 'Manufacturer') -> str:
        return f'{self.name} {self.country}'


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField('Driver')

    def __str__(self: 'Car') -> str:
        return f'{self.model} {self.manufacturer}'


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self: 'Driver') -> str:
        return self.license_number
