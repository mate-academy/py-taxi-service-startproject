from django.conf import settings

from django.contrib.auth.models import AbstractUser

from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, blank=False, null=False)
    username = models.CharField(max_length=255, blank=True, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"


class Car(models.Model):
    model = models.CharField(max_length=255, blank=True, null=True)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="car"
    )

    class Meta:
        ordering = ("model", )

    def __str__(self):
        return f"{self.model} ({self.manufacturer})"
