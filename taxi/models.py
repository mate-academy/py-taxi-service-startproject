from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=55, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars", blank=True
    )

    def __str__(self):
        return f"{self.model} ({self.manufacturer.name})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=55, unique=True)
    country = models.CharField(max_length=55, default="Unknown")  # default задаёт значение для новых и существующих записей

    def __str__(self):
        return self.name

