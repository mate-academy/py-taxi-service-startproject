from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="car", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="car")

    def __str__(self):
        return self.model

    class Meta:
        ordering = ["model"]