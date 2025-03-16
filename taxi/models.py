from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ManyToManyField



class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Drivers"
        verbose_name = "Driver"

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cars')


