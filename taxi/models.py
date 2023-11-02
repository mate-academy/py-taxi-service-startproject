from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return (f"name: {self.name},"
                f" country: {self.country}")


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(to=Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def __str__(self) -> str:
        return f"model: {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        unique_together = ["license_number"]

    def __str__(self) -> str:
        return (f"{self.username},"
                f" {self.first_name},"
                f" {self.last_name}")
