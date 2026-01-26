# taxi/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

# Modelo Manufacturer
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

# Modelo Driver (Herdando de AbstractUser)
class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        # Garante que o nome exibido seja legível
        return f"{self.get_full_name() or self.username} ({self.license_number})"

# Modelo Car
class Car(models.Model):
    model = models.CharField(max_length=100)
    license_plate = models.CharField(max_length=20, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name='cars'
    )

    def __str__(self):
        return f"{self.manufacturer.name} {self.model} ({self.license_plate})"
