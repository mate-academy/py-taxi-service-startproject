from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        "Manufacturer",
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model", )

    def __str__(self):
        return self.model


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255,
        unique=True,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
