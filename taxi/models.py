from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=160, unique=True)
    country = models.CharField(max_length=56)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=35, unique=True)
    username = models.CharField(max_length=35, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=150)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)

    class Meta:
        ordering = ("first_name",)

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=49)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="manufacturer"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
