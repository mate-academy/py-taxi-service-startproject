from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.CASCADE,
        related_name="manufacturers"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers"
    )

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
