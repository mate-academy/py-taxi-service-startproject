from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField("Driver",
                                     related_name="cars")

    def __str__(self):
        return f"{self.manufacturer} - {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100,
                                      unique=True)
