from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=[
                    "name",
                ],
                name="unique_name",
            )
        ]

    def __str__(self):
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=[
                    "license_number",
                ],
                name="unique_license_number",
            )
        ]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField("Driver", related_name="cars")
