from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name: str = models.CharField(max_length=255, unique=True)
    country: str = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number: str = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("username",)

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model: str = models.CharField(max_length=255)
    manufacturer: Manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars",
        blank=True,
    )

    class Meta:
        ordering = ("model",)

    def __str__(self) -> str:
        return self.model
