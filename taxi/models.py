from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["name"],
                name="Unique Manufacturer name"
            )
        ]

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.manufacturer.name} - {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    verbose_name = "driver"
    verbose_name_plural = "drivers"

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["license_number"],
                name="Unique license number"
            )
        ]
