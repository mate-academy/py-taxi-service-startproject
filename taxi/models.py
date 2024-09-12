from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models. CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}, {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username}, {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.model}, {self.manufacturer.name}"
