from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE,
        blank=True,
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
        blank=True
    )

    def __str__(self):
        return self.model
