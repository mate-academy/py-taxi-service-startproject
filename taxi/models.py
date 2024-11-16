from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )
        ]

    def __str__(self) -> str:
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number"
            )
        ]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self) -> str:
        return self.model
