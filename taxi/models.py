from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.DO_NOTHING,
        related_name="cars")
    driver = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name="cars")

    def __str__(self) -> str:
        return self.model
