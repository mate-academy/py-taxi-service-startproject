from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
