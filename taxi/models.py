from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True
    )

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ("username", )

    def __str__(self) -> str:
        return (f"{self.username}: "
                f"({self.first_name} {self.last_name})")


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
        ordering = ("model", )

    def __str__(self) -> str:
        return self.model