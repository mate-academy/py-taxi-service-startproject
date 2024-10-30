from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver")

    def __str__(self):
        return self.model


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
