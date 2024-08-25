from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"name: {self.name}, country: {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ("license_number",)

    def __str__(self):
        return (
            f"license number: {self.license_number}, "
            f"username: {self.username}, "
            f"first_name: {self.first_name}, "
            f"last_name: {self.last_name}"
        )


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("manufacturer",)

    def __str__(self):
        return f"Manufacturer: {self.manufacturer} - Model: {self.model}"
