from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=256, unique=True)
    country = models.CharField(max_length=256)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=256)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=256, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"
