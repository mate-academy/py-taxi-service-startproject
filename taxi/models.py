from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ('name', )

    def __str__(self: Any) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('username', )

    def __str__(self: Any) -> str:
        return self.username + ': ' + self.first_name + ' ' + self.last_name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    drivers = models.ManyToManyField(Driver, related_name='cars')

    class Meta:
        ordering = ('model', )

    def __str__(self: Any) -> str:
        names = ', '.join([driver.username for driver in self.drivers.all()])
        return self.model + ' (Drivers: ' + names + ')'
