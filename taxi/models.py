from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name} (country: {self.country})"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(to=Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    def __str__(self) -> str:
        return f"Model:{self.model}, manufacturer: {self.manufacturer}"




