from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(unique=True)


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    drivers = models.ManyToManyField(Driver, related_name="cars")