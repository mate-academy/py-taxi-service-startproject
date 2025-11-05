from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings  # ✅ ADD THIS IMPORT


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"  # ✅ ADD related_name
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,  # ✅ USE THIS instead of Driver
        related_name="cars"
    )

    def __str__(self):
        return self.model

    class Meta:
        ordering = ["model"]
        verbose_name = "car"
        verbose_name_plural = "cars"
