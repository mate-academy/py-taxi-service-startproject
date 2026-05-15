from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="cars")


class Manufacturer(models.Model):
    name = models.CharField(max_length=255,
                            null=False,
                            blank=False,
                            unique=True
                            )
    country = models.CharField(max_length=255, null=False, blank=False)


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=255, null=False, blank=False, unique=True
    )
