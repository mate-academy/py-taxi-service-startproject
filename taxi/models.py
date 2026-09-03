from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)
#    username = models.CharField(max_length=63)
#    email = models.CharField(max_length=63)
#    password = models.CharField(max_length=63)
#    first_name = models.CharField(max_length=63)
#    last_name = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
