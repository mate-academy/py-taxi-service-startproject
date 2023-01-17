from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):

    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):

    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.manufacturer} -> {self.model}"


class Driver(AbstractUser):

    license_number = models.CharField(
        max_length=255, null=True, blank=True, unique=True
    )

    class Meta:
        ordering = ["username"]
        # verbose_name = ["driver"]
        # verbose_name_plural = ["drivers"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
