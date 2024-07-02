from django.db import models
from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ("name",)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ("username",)
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers"
    )

    def __str__(self) -> str:
        return self.model

    class Meta:
        ordering = ("model",)
