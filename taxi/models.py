from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name

class Driver(AbstractUser):
    license_number = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"

class Car(models.Model):
    model = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField("Driver", max_length=120, related_name="cars")

    def __str__(self):
        return f"{self.model} ({self.manufacturer})"
