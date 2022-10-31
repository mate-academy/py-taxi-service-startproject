from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "All manufacturers"

    def __str__(self):
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "All drivers"

    def __str__(self):
        return f"{self.username} {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=65)
    manufactured = models.ForeignKey(
        Manufacturer,
        on_delete=models.SET_NULL,
        null=True
    )
    drivers = models.ManyToManyField(Driver)

    class Meta:
        verbose_name_plural = "All cars"

    def __str__(self):
        return f"{self.model}"
