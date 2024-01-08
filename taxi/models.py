from django.contrib.auth.models import AbstractUser
from django.db import models

import taxiservice.settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.DO_NOTHING,
                                     related_name="manufacturers",
                                     )
    drivers = models.ManyToManyField(taxiservice.settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ("model",)
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return self.username
