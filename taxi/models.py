from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=120)
    country = models.CharField(max_length=120)


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=120)


class Car(models.Model):
    model = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
