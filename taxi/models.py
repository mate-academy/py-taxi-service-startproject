from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = ForeignKey(to= Manufacturer, on_delete=models.CASCADE, unique=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.license_number