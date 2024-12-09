from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    class Meta:
        ordering = ("license_number",)

    def __str__(self):
        return (
            f"{self.license_number} ("
            f"username:{self.username},"
            f" email:{self.email},"
            f" first_name:{self.first_name},"
            f" last_name:{self.last_name}"
            f")"
        )


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
    )

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return self.model
