from django.db import models
from django.conf import settings
from django.db.models import CharField
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, blank=False)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
