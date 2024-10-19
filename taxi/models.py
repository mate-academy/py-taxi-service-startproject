from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", ],
                                    name="unique_manufacturer_name"
                                    ),
        ]
        ordering = ("name", )

    def __str__(self):
        return self.name, "(", self.country, ")"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["license_number", ],
                                    name="unique_driver_license_number"
                                    ),
        ]
        ordering = ("username",)

    def __str__(self):
        return (f"{self.username}: {self.first_name} "
                f"{self.last_name} ({self.license_number})")
