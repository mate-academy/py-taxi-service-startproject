from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
        verbose_name="License",
    )

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
