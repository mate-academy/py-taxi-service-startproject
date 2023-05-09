from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(
                fields=["name"],
                name="uniq_manufacturer_name"
            )
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return f"{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
    )

    class Meta:
        ordering = ["username"]
        constraints = [
            UniqueConstraint(
                fields=["license_number"],
                name="uniq_license_number"
            )
        ]

    def __str__(self) -> str:
        return f"{self.username}: " \
               f"({self.first_name} {self.last_name})"
