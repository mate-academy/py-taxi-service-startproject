from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=128, unique=True)



class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)
    country = models.CharField(max_length=128)


class Car(models.Model):
    model = models.CharField(max_length=128)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")
