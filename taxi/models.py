from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ('name',)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        ordering = ('username',)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name='cars'
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
