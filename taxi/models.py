from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):

    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class Car(models.Model):

    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField("Driver")


class Driver(AbstractUser):

    license_number = models.CharField(max_length=100, unique=True)