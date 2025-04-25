from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ManyToManyField

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=63)
    drivers = ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.model}: {self.manufacturer.name}"

    class Meta:
        ordering = ["model"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.username
