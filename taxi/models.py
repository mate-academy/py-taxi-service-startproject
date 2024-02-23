from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=65, unique=True, blank=True)

    class Meta:
        verbose_name = "Driver"

    def __str__(self):
        return self.username


class Manufacturer(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=65)

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=65)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return self.model
