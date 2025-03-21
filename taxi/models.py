from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=100,
        unique=True)

    def __str__(self):
        return (f"{self.username} - "
                f"{self.first_name} "
                f"{self.last_name}: "
                f"{self.license_number}")


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='manufactured_cars')
    drivers = models.ManyToManyField(
        Driver,
        related_name='driven_cars')

    def __str__(self):
        return self.model