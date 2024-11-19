from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="driver_groups",
        blank=True
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="driver_permissions",
        blank=True
    )

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
