from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, related_name="manufacturers", on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model
