from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.DO_NOTHING,
        null=True,
        related_name="cars"
    )
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name="cars")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
