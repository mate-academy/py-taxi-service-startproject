from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

    class Meta:
        ordering = ["name"]

    def _str_(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=60)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="car_range"
    )
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="my_cars")

    class Meta:
        ordering = ["model"]

    def _str_(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=60, unique=True, null=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
