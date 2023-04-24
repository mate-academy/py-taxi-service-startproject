from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.TextField(unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()

    class Meta:
        ordering = ["name"]


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.DO_NOTHING,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="cars"
    )
