from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("-country", )

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    class Meta:
        ordering = ("model", )

    def __str__(self):
        drivers_str = ", ".join(str(driver) for driver in self.drivers.all())
        return f"{self.manufacturer.name} {self.model} ({drivers_str})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
