from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver)

    def __str__(self) -> str:
        return self.model

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
        verbose_name = "drivers"
