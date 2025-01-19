from django.db import models

from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=70, unique=True)
    country = models.CharField(max_length=70)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return f"{self.name}({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=70)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=70, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
