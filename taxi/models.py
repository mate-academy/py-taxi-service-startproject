from django.db import models
from taxi_service import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
