from tkinter.constants import CASCADE

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.model} produced in {self.manufacturer}"

class Manufacturer(models.Model):
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"Manufacturer {self.name} in {self.country}"

class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)
