from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=60, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ["name",]

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=40, unique=True)

    class Meta:
        ordering = ["username",]


class Car(models.Model):
    model = models.CharField(max_length=60)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars")
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["model",]

    def __str__(self):
        return self.model
