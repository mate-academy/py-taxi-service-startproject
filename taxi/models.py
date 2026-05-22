from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name='cars')
    driver = models.ForeignKey("Driver", on_delete=models.CASCADE, related_name='cars')

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}, ({self.manufacturer.name})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username}, ({self.license_number})"
