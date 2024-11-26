from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model",)
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
