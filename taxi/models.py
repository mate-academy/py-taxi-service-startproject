from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=127)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number",
            )
        ]
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username}, ({self.first_name}, {self.last_name})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=127)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_manufacturer",
            )
        ]
        ordering = ["name"]

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return self.model
