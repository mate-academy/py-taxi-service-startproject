from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=65,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Driver"


class Car(models.Model):
    model = models.CharField(max_length=265)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(Driver, related_name="books")

