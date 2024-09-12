from django.db import models
from django.conf import settings
from django.db.models import UniqueConstraint
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["licence_number"],
                name="unique_licence_number"
            )
        ]
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL
    )
