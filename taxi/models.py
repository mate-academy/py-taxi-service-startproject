from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return self.model

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"