from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=25, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Cars")
