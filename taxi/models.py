from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)
    
    class Meta:
        ordering = ("username", )
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        ordering =  ("name", )


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self):
        return self.model

    class Meta:
        ordering =  ("model", )
