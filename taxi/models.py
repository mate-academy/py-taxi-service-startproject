from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=256,
        unique=True,
        null=True,
        blank=True
    )
    password = models.CharField(max_length=256)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=256, unique=True)
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=256)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers"
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="manufacturers"
    )

    def __str__(self):
        return self.manufacturer.name + " " + str(self.model)
