from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, related_name='cars')
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name='cars')

    def __str__(self):
        return self.model


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "drivers"

    def __str__(self):
        return self.username
