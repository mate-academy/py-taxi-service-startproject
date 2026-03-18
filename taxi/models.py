from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cars')