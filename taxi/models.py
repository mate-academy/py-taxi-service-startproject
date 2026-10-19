from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=8, unique=True)

    def __str__(self) -> str:
        return self.username
