from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"

    class Meta:
        ordering = ("name", "country")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    class Meta:
        ordering = ("username",)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self) -> str:
        return f"{self.model} ({self.manufacturer})"

    class Meta:
        ordering = ("model",)
