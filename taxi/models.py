from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        constraints = [
            UniqueConstraint(fields=["name"], name="unique_name")
        ]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ["username"]
        constraints = [
            UniqueConstraint(fields=["license_number"], name="unique_number")
        ]
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="manufacturer")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model} (manufacturer: {self.manufacturer})"

