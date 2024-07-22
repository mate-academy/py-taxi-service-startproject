from taxi_service import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars", )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers", )

    def __str__(self):
        return f"{self.model}"
