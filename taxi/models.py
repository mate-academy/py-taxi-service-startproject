from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
        blank=True,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"

    class Meta:
        ordering = ("username",)


class Car(models.Model):
    model = models.CharField(max_length=255)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    class Meta:
        ordering = ("model",)

    def __str__(self) -> str:
        return f"{self.model} driver: {self.drivers}"
