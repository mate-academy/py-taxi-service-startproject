from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service import settings


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.DO_NOTHING, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.model} - {self.manufacturer}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ("first_name",)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
