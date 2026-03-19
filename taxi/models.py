from django.contrib.auth.models import AbstractUser
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Driver(AbstractUser):
    license_number = models.CharField(unique=True)
    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="drivers")