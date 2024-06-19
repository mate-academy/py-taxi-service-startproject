from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        default=None
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='cars',
    )

    def __str__(self) -> str:
        return F"{self.model} {self.manufacturer} {self.drivers}"
