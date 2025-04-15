from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.TextField()

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars"
    )


class Driver(AbstractUser):
    license_number = models.TextField()

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
