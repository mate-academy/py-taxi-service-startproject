from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacture(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacture = models.ForeignKey(
        "Manufacture", on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField("Driver", related_name="cars")

    class Meta:
        ordering = ["manufacture__name", "model"]

    def __str__(self):
        return f"{self.manufacture.name} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"