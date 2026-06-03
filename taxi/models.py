from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        default="",
        unique=True,
    )

    def __str__(self) -> str:
        return f'{self.username} {self.license_number}'

    class Meta:
        ordering = ['username',]


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name='cars')

    def __str__(self) -> str:
        return f'{self.manufacturer} {self.model}'
