from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(AUTH_USER_MODEL)

    def __str__(self) -> str:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)
    is_staff = models.BooleanField(
        "staff status",
        default=True,
        help_text="Designates whether the user can log into this admin site.",
    )

    class Meta:
        verbose_name_plural = "drivers"
        swappable = 'AUTH_USER_MODEL'

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
