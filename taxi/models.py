from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return (
            f"{self.username}: ({self.first_name} {self.last_name}). "
            f"License number: {self.license_number}"
        )


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="manufacturer", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name="drivers",
        blank=True,
    )

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"
