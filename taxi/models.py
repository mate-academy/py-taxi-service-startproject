from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models import CharField


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
    )

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> CharField:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
    manufacturer = models.ForeignKey(Manufacturer, related_name="cars", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.manufacturer.name } {self.model}"
