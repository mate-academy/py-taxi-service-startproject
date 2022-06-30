from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
        ordering = ['license_number']

    def enable_cars(self):
        return ", ".join([car.model for car in self.cars.all()])

    def __str__(self):
        return f"{self.username}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ['model']

    def all_drivers(self):
        return ", ".join([driver.username for driver in self.drivers.all()])

