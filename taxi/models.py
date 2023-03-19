from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=31, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, related_name="cars", on_delete=models.DO_NOTHING)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
