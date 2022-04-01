from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, related_name="cars", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["license_number"],
                             name="license_should_be_unique")
        ]

        verbose_name = "driver"
        verbose_name_plural = "drivers"
