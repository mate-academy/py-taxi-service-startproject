from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    license_plate = models.CharField(max_length=10, unique=True)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
