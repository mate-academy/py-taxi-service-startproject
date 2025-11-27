from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = "manufacturer"
        indexes = [
            models.Index(fields=["name"]),
        ]

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=16, unique=True)

    class Meta:
        db_table = "drivers"
        indexes = [
            models.Index(fields=["license_number"]),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"
