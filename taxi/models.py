from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):  #
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} by {self.manufacturer.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.license_number})"
