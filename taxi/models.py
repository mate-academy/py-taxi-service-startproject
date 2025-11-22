from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name="cars",
        blank=True,
    )

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return self.model
