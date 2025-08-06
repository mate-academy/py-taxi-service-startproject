from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ManyToManyField


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True
    )
    country = models.CharField(
        max_length=255
    )
    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True
    )
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='taxi_drivers',
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='taxi_drivers',
        blank=True,
    )

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return (f"{self.username} "
                f"({self.first_name} "
                f"{self.last_name})")

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = ManyToManyField(
        Driver,
        related_name="cars")

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model
