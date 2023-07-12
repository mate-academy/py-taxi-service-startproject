from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_manufacturer"
            )
        ]

    def __str__(self) -> str:
        return f"Name: {self.name} Country: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.DO_NOTHING,
        related_name="cars"
    )
    driver = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self) -> str:
        return f"Model: {self.model} Manufacturer: {self.manufacturer}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number"
            )
        ]
