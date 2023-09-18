from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    class Meta:
        indexes = [
            models.Index(fields=["model"]),
            models.Index(fields=["manufacturer"]),
        ]
        ordering = ["model"]

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"
