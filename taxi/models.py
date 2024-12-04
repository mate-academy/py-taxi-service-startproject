from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField('Driver', related_name='cars')


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

