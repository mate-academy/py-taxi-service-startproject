from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
