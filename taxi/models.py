from django.db import models
from taxi_service import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()


class Driver(AbstractUser):
    license_number = models.TextField(unique=True)
    # username = models.TextField()
    # email = models.TextField()
    # password = models.TextField()
    # first_name = models.TextField()
    # last_name = models.TextField()


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
