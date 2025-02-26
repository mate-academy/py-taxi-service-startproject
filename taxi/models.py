from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, verbose_name="cars"
    )
    drivers = models.ManyToManyField(Driver, verbose_name="cars")
