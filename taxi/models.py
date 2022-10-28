from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        related_name="manufacturer",
        on_delete=models.CASCADE,
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="driver",
    )
