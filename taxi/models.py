
from django.contrib.auth.models import AbstractUser
from django.db import models


from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    coutry = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars"
    )
