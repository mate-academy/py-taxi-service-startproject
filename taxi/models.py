from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=100, default="Unknown")

    class Meta:
        ordering = ("name", )
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=69, unique=True)

    class Meta:
        ordering = ("last_name", "first_name", )
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.last_name} {self.first_name}: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model", )
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"
