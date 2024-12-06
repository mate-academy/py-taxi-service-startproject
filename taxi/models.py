from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=64, unique=True)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    class Meta:
        ordering = ["manufacturer", "model"]

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return  f"{self.first_name}, {self.last_name}"