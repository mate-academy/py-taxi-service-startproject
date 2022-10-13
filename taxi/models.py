from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=150)

    class Meta:
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_manufacturer_name"
            )
        ]

    def __str__(self):
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"],
                name="unique_driver_license",
            )
        ]

    def __str__(self):
        return f"{self.username} license: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}"
