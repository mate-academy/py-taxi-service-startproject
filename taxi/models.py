from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service.settings import AUTH_USER_MODEL

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", related_name="cars", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return self.model

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"