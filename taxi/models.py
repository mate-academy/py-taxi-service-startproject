from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True,)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
    )

    def __str__(self):
        return f"{self.manufacturer}: {self.model}"
