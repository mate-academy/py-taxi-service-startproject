from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()


class Driver(AbstractUser):
    license_number = models.CharField(unique=True)
    class Meta:
        pass


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ForeignKey(Driver, on_delete=models.CASCADE)
