from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    country = models.CharField(max_length=60)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=60)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return (f"{self.first_name} {self.last_name} "
                f"{self.username} {self.license_number}")
