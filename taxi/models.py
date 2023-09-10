from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True,
    )
    county = models.CharField(
        max_length=100,
    )

    def __str__(self) -> str:
        return f"Name: {self.name}, country: {self.county}"


    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"<Name: {self.name}, country: {self.county}>"


class Driver(AbstractUser):
    username = models.CharField(
        max_length=100,
        unique=True)
    license_number = models.CharField(
        max_length=100,
        unique=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        ordering = ("username", )
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars")
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"<Model: {self.model}, manufacturer: {self.manufacturer.name}>"
