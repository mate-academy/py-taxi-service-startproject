from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Driver(AbstractUser):
    license_number = models.CharField(max_length=11, unique=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    country = models.CharField(max_length=100)


class Car(models.Model):
    model = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(Driver, related_name="cars")
