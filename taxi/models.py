from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return f"{self.name}: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=20)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.DO_NOTHING, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> CharField:
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ("last_name",)
