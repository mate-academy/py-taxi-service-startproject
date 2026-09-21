from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name", )
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        "Manufacturer",
        related_name="cars",
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model", )
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True, null=True)

    class Meta:
        ordering = ("username", )
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"
