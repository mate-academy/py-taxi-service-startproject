from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('name',)
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
