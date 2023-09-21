from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
