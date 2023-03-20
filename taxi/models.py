from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["country", "name"]

    def __str__(self) -> str:
        return f"Name: {self.name}, Country: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return f"Model: {self.model}, manufacturer: {self.manufacturer.name}"


class Driver(AbstractUser):

    license_number = models.CharField(max_length=255, unique=True)


    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"


