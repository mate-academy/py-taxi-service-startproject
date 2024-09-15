from django.contrib.auth.models import AbstractUser
from django.db import models

from django.conf import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self) -> str:
        return f"{self.username}: {self.first_name} {self.last_name}"


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True
    )
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ("name", )

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=50)
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
        ordering = ("manufacturer", "model", )

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
