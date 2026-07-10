from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    drivers = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="cars"
    )

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        return self.username
