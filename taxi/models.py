from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "Driver license"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers",
    )
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model} {self.manufacturer}"
