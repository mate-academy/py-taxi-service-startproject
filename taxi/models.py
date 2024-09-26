from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return (
            f"{self.username} ({self.first_name} {self.last_name}), "
            f"license number: {self.license_number}"
        )


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="manufacturers"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
