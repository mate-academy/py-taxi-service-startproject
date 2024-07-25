from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    format = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ('format', 'country',)

    def __str__(self) -> str:
        return self.format


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='cars'
    )

    class Meta:
        ordering = ('model',)

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    class Meta:
        ordering = ('license_number', 'username',)

