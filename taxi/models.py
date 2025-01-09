from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=50)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"
