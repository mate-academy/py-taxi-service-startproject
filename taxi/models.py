from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=66, unique=True)
    country = models.CharField(max_length=20)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=66, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
