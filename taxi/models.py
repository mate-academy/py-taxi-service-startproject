from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=250, unique=True)
    country = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=250)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ("model", )

    def __str__(self) -> str:
        return f"Car: {self.manufacturer} - {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=250,
                                      unique=True,
                                      blank=True,
                                      null=True)
    password = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self) -> str:
        return f"Driver: {self.license_number}"
