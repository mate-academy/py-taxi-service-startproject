from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ["country", "name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey("Manufacturer",
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def enable_drivers(self):
        return ", ".join([driver.username for driver in self.drivers.all()])

    def __str__(self):
        return f"{self.model} - {self.manufacturer}"


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=63, unique=True)

    def enable_cars(self):
        return ", ".join([car.model for car in self.cars.all()])

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
