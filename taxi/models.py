from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, related_name="cars", on_delete=models.CASCADE)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.model} ({self.manufacturer.name})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
