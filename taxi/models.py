from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=65)

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=65, unique=True)

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=65)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model

