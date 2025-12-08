from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63, blank=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    class Meta:
        ordering = ("name",)


class Car(models.Model):
    model = models.CharField(max_length=63, blank=True)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"

    )

    def __str__(self) -> str:
        return f"{self.model}"

    class Meta:
        ordering = ("model",)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        ordering = ("license_number",)
