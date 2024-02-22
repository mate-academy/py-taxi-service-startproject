from django.db import models

from django.contrib.auth.models import AbstractUser

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        ordering = ("name",)


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars"
                                     )
    model = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.model} ({self.manufacturer})"

    class Meta:
        ordering = ("model",)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name} {self.license_number}"

    class Meta:
        ordering = ("username",)
