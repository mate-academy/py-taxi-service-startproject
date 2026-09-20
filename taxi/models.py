from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "manufacturers"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "drivers"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="manufacturers")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name="drivers")

    class Meta:
        verbose_name = "cars"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return self.model
