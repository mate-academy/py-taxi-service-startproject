from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from taxi_servise import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["license_number"],
                             name="license_number_is_unique")
        ]

        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="manufacturers"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.model} {self.manufacturer}"
