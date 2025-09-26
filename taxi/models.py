from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:  # simples, estilo checklist
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    # campos exigidos ao criar superuser pelo createsuperuser
    REQUIRED_FIELDS = ["email", "license_number"]

    # Meta após atributos de classe (conforme checklist)
    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    # usar AUTH_USER_MODEL (conforme checklist)
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
        blank=True,
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return self.model
