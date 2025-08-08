from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    license_number = models.CharField(
        unique=True,
        max_length=20
    )

    class Meta:
        ordering = ("license_number",)
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.license_number}: {self.first_name} {self.last_name}"


class Manufacturer(models.Model):
    name = models.CharField(
        unique=True, max_length=63
    )
    country = models.CharField(
        max_length=63
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return self.name


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
        ordering = ("model",)
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"