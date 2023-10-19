from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255, unique=True
    )

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.PROTECT,
        related_name="manufacturer"
    )
    drivers = models.ManyToManyField(
        get_user_model(),
        related_name="drivers",
        blank=True
    )

    def __str__(self):
        return self.model
