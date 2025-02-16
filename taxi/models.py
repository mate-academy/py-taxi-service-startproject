from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)  # Unique constraint
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)  # Unique constraint

    def __str__(self):
        return f"{self.username} ({self.license_number})"

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self):
        return f"{self.model} - {self.manufacturer.name}"
