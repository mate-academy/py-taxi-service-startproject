from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     blank=True,
                                     related_name="cars"
                                     )

    def __str__(self):
        return f"{self.manufacturer} ({self.model})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            unique=True
                            )
    country = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255, null=False, blank=False, unique=True
    )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
