from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        verbose_name="license number"
    )

    class Meta:
        verbose_name_plural = "driver with license"


class Car(models.Model):
    model = models.CharField(max_length=65)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return self.model
