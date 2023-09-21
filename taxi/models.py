from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True, db_index=True)
    country = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ("name",)
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_manufacturer_name")
        ]

    def __str__(self) -> str:
        return f"{self.name}" f"{self.country} "


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=255, db_index=True)
    additional_info = models.CharField(max_length=255, db_index=True, default="")

    class Meta:
        ordering = ("username",)
        constraints = [
            models.UniqueConstraint(
                fields=["license_number", "password", "additional_info"],
                name="unique_driver_license_number",
            )
        ]

    def update_license_number(self, new_license_number, password, additional_info):
        self.license_number = new_license_number
        self.password = password
        self.additional_info = additional_info
        self.save()


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ManyToManyField(to=Manufacturer)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.model} {self.manufacturer} {self.drivers}"
