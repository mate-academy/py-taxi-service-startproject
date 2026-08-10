from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_sevice import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"name: {self.name}, country: {self.country}"

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)
    model = models.CharField(max_length=63)

    def __str__(self):
        return f"model: {self.model}, country: {self.manufacturer.country}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
