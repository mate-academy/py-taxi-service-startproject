from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=50)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, unique=True)


class Car(models.Model):

    model = models.CharField(max_length=25)

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )

    drivers = models.ManyToManyField(Driver)
