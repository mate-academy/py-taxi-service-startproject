from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, null=True, max_length=55)
