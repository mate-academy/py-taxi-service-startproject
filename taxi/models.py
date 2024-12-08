from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        constraints = [
            UniqueConstraint(
                fields=["name", ],
                name="unique_manufacturer_name",
            ),
        ]

    def __str__(self):
        return f"{self.name}, {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["license_number", ],
                name='unique_license_number',
            ),
        ]

    def __str__(self):
        return (f"{self.username} ({self.first_name} {self.last_name}, "
                f"#{self.license_number})")


class Car(models.Model):
    model = models.CharField(max_length=255, default="Default Model")
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.model}, {self.manufacturer}, {self.drivers}"
