from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_name")
        ]
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=65)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"], name="license_number"
            )
        ]

        ordering = ["username"]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="manufacturers"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers")

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return self.model
