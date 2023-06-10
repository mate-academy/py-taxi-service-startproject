from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)

    def __str__(self) -> str:
        return str(self.name)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=250, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return str(self.username)


class Car(models.Model):
    model = models.CharField(max_length=250)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="manufacturer"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    def __str__(self) -> str:
        return str(self.model)
