from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, unique=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


