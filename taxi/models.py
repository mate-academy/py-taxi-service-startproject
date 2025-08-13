from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


NAME_MAX_LENGTH = 63
COUNTRY_MAX_LENGTH = 63
MODEL_MAX_LENGTH = 63
LICENSE_MAX_LENGTH = 63


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=LICENSE_MAX_LENGTH,
        unique=True
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}".strip()
        return f"{self.username}: ({full_name})" if full_name else self.username


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True
    )
    country = models.CharField(max_length=COUNTRY_MAX_LENGTH)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=MODEL_MAX_LENGTH)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model",)
        constraints = [
            models.UniqueConstraint(
                fields=("manufacturer", "model"),
                name="unique_model_per_manufacturer"
            )
        ]

    def __str__(self):
        return f"{self.model} ({self.manufacturer.name})"
