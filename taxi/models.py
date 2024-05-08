from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE,
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model", )

    def __str__(self) -> str:
        return f"{self.model} made by {self.manufacturer.name}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
