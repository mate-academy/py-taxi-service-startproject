from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=200, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='cars')
