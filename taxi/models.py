from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Model, UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["licence_number"], name="unique_licence_number")
        ]
        verbose_name = "driver"
        verbose_name_plural = "drivers"
