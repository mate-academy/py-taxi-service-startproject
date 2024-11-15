from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.country}"

    class Meta:
        verbose_name_plural = "manufacturers"
        ordering = ("name", "country", )


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="cars",
        on_delete=models.CASCADE
    )


    class Meta:
        ordering = ("model", )
        verbose_name_plural = "cars"


    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "drivers"
